#!/usr/bin/env python

import click
from click.testing import CliRunner
from clikan import configure, clikan, new, promote, display, regress, remove
import os

## Configure Tests

def test_command_help():
    runner = CliRunner()
    result = runner.invoke(clikan, ["--help"])
    assert result.exit_code == 0
    assert 'Usage: clikan [OPTIONS] COMMAND [ARGS]...' in result.output
    assert 'clikan: CLI personal kanban' in result.output

def test_command_version():
    version_file = open(os.path.join('./', 'VERSION'))
    version = version_file.read().strip()

    runner = CliRunner()
    result = runner.invoke(clikan, ["--version"])
    assert result.exit_code == 0
    assert 'clikan, version {}'.format(version) in result.output

def test_command_configure():
    runner = CliRunner()
    result = runner.invoke(clikan, ["configure"])
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
    result = runner.invoke(clikan, ["n", "--task", "n_--task_test"])
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

## Display Tests
def test_command_d():
    runner = CliRunner()
    result = runner.invoke(clikan, ["d"])
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
    result = runner.invoke(clikan, ['promote', '--id', '1'])
    assert result.exit_code == 0
    assert 'Promoting task 1 to in-progress.' in result.output
    result = runner.invoke(clikan, ['promote', '--id', '1'])
    assert result.exit_code == 0
    assert 'Promoting task 1 to done.' in result.output

## Remove Tests
def test_command_delete():
    runner = CliRunner()
    result = runner.invoke(clikan, ['remove', '--id', '1'])
    assert result.exit_code == 0
    assert 'Removed task 1.' in result.output
    result = runner.invoke(clikan, ['remove', '--id', '1'])
    assert result.exit_code == 0
    assert 'No existing task with' in result.output
