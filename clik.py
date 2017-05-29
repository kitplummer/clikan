import click
import yaml
import os

@click.command()
def cli():
    print "clik world!"
    config = read_config()
    print config

def read_config():
    with open(os.environ['HOME'] + "/.clik.yaml", 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print "Ensure ~/.clik.yaml exists."
            print(exc)
