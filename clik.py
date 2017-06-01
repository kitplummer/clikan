import click
import yaml
import os
from terminaltables import SingleTable
import sys
from textwrap import wrap
import collections

VERSION = '0.0.1'
class Config(object):
    """The config in this example only holds aliases."""

    def __init__(self):
        self.path = os.getcwd()
        self.aliases = {}

    def read_config(self, filename):
        parser = configparser.RawConfigParser()
        parser.read([filename])
        try:
            self.aliases.update(parser.items('aliases'))
        except configparser.NoSectionError:
            pass


pass_config = click.make_pass_decorator(Config, ensure=True)

class AliasedGroup(click.Group):
    """This subclass of a group supports looking up aliases in a config
    file and with a bit of magic.
    """

    def get_command(self, ctx, cmd_name):
        # Step one: bulitin commands as normal
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv

        # Step two: find the config object and ensure it's there.  This
        # will create the config object is missing.
        cfg = ctx.ensure_object(Config)

        # Step three: lookup an explicit command aliase in the config
        if cmd_name in cfg.aliases:
            actual_cmd = cfg.aliases[cmd_name]
            return click.Group.get_command(self, ctx, actual_cmd)

        # Alternative option: if we did not find an explicit alias we
        # allow automatic abbreviation of the command.  "status" for
        # instance will match "st".  We only allow that however if
        # there is only one command.
        matches = [x for x in self.list_commands(ctx)
                   if x.lower().startswith(cmd_name.lower())]
        if not matches:
            return None
        elif len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])
        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))

def read_config(ctx, param, value):
    """Callback that is used whenever --config is passed.  We use this to
    always load the correct config.  This means that the config is loaded
    even if the group itself never executes so our aliases stay always
    available.
    """
    cfg = ctx.ensure_object(Config)
    if value is None:
        value = os.path.join(os.path.dirname(__file__), 'aliases.ini')
    cfg.read_config(value)
    return value

@click.command(cls=AliasedGroup)
def cli():
    """ CLIK CLI personal kanban """

@cli.command()
@click.option('--todo', prompt=True)
def new(todo):
    """Create new todo"""
    click.echo('Creating new todo w/ %s' % todo)
    config = read_config_yaml()
    dd = read_data(config)
    #print "DD: %r" % dd
    od = collections.OrderedDict(sorted(dd.items()))
    #print "ID: %r" % od

    print "New: %r" % {next(reversed(od))+1:['todo', todo]}
    dd[next(reversed(od))+1] = ['todo', todo]
    print "DD: %r" % dd
    write_data(config, dd)

@cli.command()
@click.option('--id', prompt=True)
def remove(id):
    """Remove todo"""
    config = read_config_yaml()
    dd = read_data(config)
    click.echo('Remove todo: %r' % dd.get(int(id)))
    dd.pop(int(id))
    write_data(config, dd)

@cli.command()
def display():
    """clik display"""

    config = read_config_yaml()

    # dd = {1: ['todo', 'todo1'],
    #       6: ['todo', 'this is a longer todoodoo'],
    #       7: ['todo', 'another longbamabobadoodleydood'],
    #       2: ['inprogress', 'ip1'],
    #       8: ['inprogress', 'workin on dis!'],
    #       3: ['done', 'done1'],
    #       4: ['done', 'done2'],
    #       5: ['done', 'doneski but tis a long thingermabob that goes on.']
    #       }

    dd = read_data(config)

    todos = []
    inprogs = []
    dones = []
    for key, value in dd.iteritems():
        if value[0] == 'todo':
            todos.append( "[%d] %s" % (key, value[1]) )
        elif value[0] == 'inprogress':
            inprogs.append( "[%d] %s" % (key, value[1]) )
        else:
            dones.append( "[%d] %s" % (key, value[1]) )


    todos = '\n'.join([str(x) for x in todos])
    inprogs = '\n'.join([str(x) for x in inprogs])
    dones = '\n'.join([str(x) for x in dones])

    td = [
        ['todo', 'in-progress', 'done'],
        ['','',''],
    ]

    table = SingleTable(td, 'clik')
    table.inner_heading_row_border = False
    table.inner_row_border = True
    table.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
    #table.padding_left = 5
    #table.padding_right = 5

    # todos wrapping
    max_width = table.column_max_width(0)

    wrapped_string = '\n'.join(['\n'.join(wrap(line, max_width,
                 break_long_words=False, replace_whitespace=False))
                 for line in todos.splitlines() if line.strip() != ''])

    table.table_data[1][0] = wrapped_string

    # inprogs wrapping
    max_width = table.column_max_width(1)
    wrapped_inprogs = '\n'.join(['\n'.join(wrap(line, max_width,
                 break_long_words=False, replace_whitespace=False))
                 for line in inprogs.splitlines() if line.strip() != ''])
    table.table_data[1][1] = wrapped_inprogs

    # dones wrapping
    max_width = table.column_max_width(2)
    wrapped_dones = '\n'.join(['\n'.join(wrap(line, max_width,
                 break_long_words=False, replace_whitespace=False))
                 for line in dones.splitlines() if line.strip() != ''])
    table.table_data[1][2] = wrapped_dones

    print(table.table)

def read_data(config):
    """Read the existing data from the config datasource"""
    with open(config["clik_data"], 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print "Ensure %s exists, as you specified it as the clik data file." % config['clik_data']
            print(exc)

def write_data(config, data):
    """Write the data to the config datasource"""
    with open(config["clik_data"], 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def read_config_yaml():
    """Read the app config from ~/.clik.yaml"""
    with open(os.environ['HOME'] + "/.clik.yaml", 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print "Ensure ~/.clik.yaml exists."
            print(exc)
