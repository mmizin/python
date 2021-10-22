import logging
from time import sleep

import urllib3

from config import DevCliConfig
from firebolt_client import FireboltClient

import pytest
import datetime

DATE_TIME = datetime.datetime.today().strftime("%Y_%m_%dT_%H_%M_%S")


@pytest.fixture(scope='session')
def dev_cli(request):
    return DevCliConfig(request)


@pytest.fixture(scope='session', autouse=True)
def fb_api():
    return FireboltClient()


@pytest.fixture(scope='session')
def setup(dev_cli_config):
    print(f"\nSetup")
    # dev_cli = dev_cli_config
    # dev_cli.create_database()
    # dev_cli.stop_engine()
    # dev_cli.edit_engine_name()
    # dev_cli.start_engine()
    yield
    print('\ntear down')


def pytest_addoption(parser):

    parser.addoption('--branch',
                     action='store',
                     help = 'branch name (string): '
                            '--branch=my_feature_branch (packdb branch - https://bitbucket.org/packdb/packdb/branches)',
                     default='master')

    parser.addoption('--commit',
                     action='store',
                     help='commit number (string): --commit=xxxxxx{8+}')

    parser.addoption('--database',
                     action='store',
                     help='existing database name (string): --database=existing_database_name',
                     default=f'pytest_db_{DATE_TIME}')

    parser.addoption('--engine_type',
                     action='store',
                     help='engine type (string): --engine_type=i3.xlarge',
                     default='i3.xlarge')

    parser.addoption('--engine_name',
                     action='store',
                     help='engine name (string): --engine_name=your_engine_name',
                     default=f'pytest_engine_{DATE_TIME}')

    parser.addoption('--region',
                     action='store',
                     help='database region (string): --region=us-east-1',
                     default='us-east-1')

    parser.addoption('--scale',
                     action='store',
                     help='engine nodes scale (int): --scale=2',
                     default=2)

    parser.addoption('--warmup_method',
                     action='store',
                     help='warmup method, type:string, '
                          'values: [minimal, indexes, all], example: --warmup_method=indexes',
                     default='indexes')

    parser.addoption('--env',
                     action='store',
                     help='environment, type: string, values: [dev, staging], example: --env=dev',
                     default='dev')

    parser.addoption('--autostop',
                     action='store',
                     help='autostop engine, type: string: values: [m, h], example: 2h30m',
                     default='20m')






