#!/usr/bin/env python

import click
from click.testing import CliRunner
from clikan import configure, clikan, add, promote, show, regress, delete
import os
import pathlib
import tempfile

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

def test_command_configure(tmp_path):
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tmpdirname:
        with runner.isolation(input=None, env={"CLIKAN_HOME" : tmpdirname}, color=False):
            result = runner.invoke(clikan, ["configure"])
            assert result.exit_code == 0
            assert 'Creating' in result.output

def test_command_configure_existing():
    runner = CliRunner()
    with runner.isolated_filesystem():
        runner.invoke(clikan, ["configure"])
        result = runner.invoke(clikan, ["configure"])

        assert 'Config file exists' in result.output

## New Tests
def test_command_a():
    runner = CliRunner()
    result = runner.invoke(clikan, ["a", "n_--task_test"])
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

## Show Tests
def test_no_command():
    runner = CliRunner()
    result = runner.invoke(clikan, [])
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

def test_command_s():
    runner = CliRunner()
    result = runner.invoke(clikan, ["s"])
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

def test_command_show():
    runner = CliRunner()
    result = runner.invoke(show)
    assert result.exit_code == 0
    assert 'n_--task_test' in result.output

def test_command_not_show():
    runner = CliRunner()
    result = runner.invoke(show)
    assert result.exit_code == 0
    assert 'blahdyblah' not in result.output

## Promote Tests
def test_command_promote():
    runner = CliRunner()
    result = runner.invoke(clikan, ['promote', '1'])
    assert result.exit_code == 0
    assert 'Promoting task 1 to in-progress.' in result.output
    result = runner.invoke(clikan, ['promote', '1'])
    assert result.exit_code == 0
    assert 'Promoting task 1 to done.' in result.output

## Delete Tests
def test_command_delete():
    runner = CliRunner()
    result = runner.invoke(clikan, ['delete', '1'])
    assert result.exit_code == 0
    assert 'Removed task 1.' in result.output
    result = runner.invoke(clikan, ['delete', '1'])
    assert result.exit_code == 0
    assert 'No existing task with' in result.output

## Repaint Tests
def test_repaint_config_option():
    runner = CliRunner()
    version_file = open(os.path.join('./', 'VERSION'))
    version = version_file.read().strip()
    path_to_config = str(pathlib.Path("./tests/repaint").resolve())
    print(path_to_config)
    with runner.isolation(input=None, env={"CLIKAN_HOME" : path_to_config}, color=False):
        result = runner.invoke(clikan, [])
        assert result.exit_code == 0
        assert 'clikan' in result.output
        result = runner.invoke(clikan, ["a", "n_--task_test"])
        assert result.exit_code == 0
        assert 'n_--task_test' in result.output
        assert version in result.output

def test_no_repaint_config_option():
    runner = CliRunner()
    version_file = open(os.path.join('./', 'VERSION'))
    version = version_file.read().strip()
    path_to_config = str(pathlib.Path("./tests/no_repaint").resolve())
    print(path_to_config)
    with runner.isolation(input=None, env={"CLIKAN_HOME" : path_to_config}, color=False):
        result = runner.invoke(clikan, [])
        assert result.exit_code == 0
        assert 'clikan' in result.output
        result = runner.invoke(clikan, ["a", "n_--task_test"])
        assert result.exit_code == 0
        assert 'n_--task_test' in result.output
        assert version not in result.output