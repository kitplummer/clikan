#!/usr/bin/env python

import click
from click.testing import CliRunner
from clikan import configure, cli, new, promote, display, regress, remove

## Configure Tests
def test_command_configure():
    runner = CliRunner()
    result = runner.invoke(cli, ["configure"])
    assert result.exit_code == 0
    assert 'Creating' in result.output

## New Tests
def test_command_new():
    runner = CliRunner()
    result = runner.invoke(new, input='testing new')
    assert result.exit_code == 0
    assert 'testing new' in result.output

def test_command_n():
    runner = CliRunner()
    result = runner.invoke(cli, ["n", "--task", "n_--task_test"])
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

## Display Tests
def test_command_d():
    runner = CliRunner()
    result = runner.invoke(cli, ["d"])
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

def test_command_display():
    runner = CliRunner()
    result = runner.invoke(display)
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

def test_command_not_display():
    runner = CliRunner()
    result = runner.invoke(display)
    assert result.exit_code == 0
    assert 'blahdyblah' not in result.output

## Promote Tests
def test_command_promote():
    runner = CliRunner()
    result = runner.invoke(cli, ['promote', '--id', '1'])
    assert result.exit_code == 0
    assert 'Promoting task 1 to in-progress.' in result.output
    result = runner.invoke(cli, ['promote', '--id', '1'])
    assert result.exit_code == 0
    assert 'Promoting task 1 to done.' in result.output

