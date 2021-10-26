import json
import subprocess
import requests

from abc import ABC


class DevCliConfig:

    def __init__(self, request):
        self.dev_cli_config = {'branch': request.config.getoption('--branch'),
                               'commit': request.config.getoption('--commit'),
                               'database': request.config.getoption('--database'),
                               'engine_type': request.config.getoption('--engine_type'),
                               'engine_name': request.config.getoption('--engine_name'),
                               'region': request.config.getoption('--region'),
                               'scale': request.config.getoption('--scale'),
                               'warmup_method': request.config.getoption('--warmup_method'),
                               'env': request.config.getoption('--env'),
                               'autostop': request.config.getoption('--autostop')
                               }

    def __repr__(self):
        return f'\nbranch: {self.dev_cli_config["branch"]}' \
               f'\ncommit: {self.dev_cli_config["commit"]}' \
               f'\ndatabase: {self.dev_cli_config["database"]}' \
               f'\nengine_type: {self.dev_cli_config["engine_type"]}' \
               f'\nengine_name: {self.dev_cli_config["engine_name"]}' \
               f'\nregion: {self.dev_cli_config["region"]}' \
               f'\nscale: {self.dev_cli_config["scale"]}' \
               f'\nwarmup_method: {self.dev_cli_config["warmup_method"]}' \
               f'\nenv: {self.dev_cli_config["env"]}' \
               f'\nautostop: {self.dev_cli_config["autostop"]}' \


    def create_database(self):
        command = f'./dev-cli create ' \
                  f'-n {self.dev_cli_config["database"]}_{self.dev_cli_config["env"]} ' \
                  f'-s {self.dev_cli_config["scale"]} ' \
                  f'-b {self.dev_cli_config["branch"]} ' \
                  f'-r {self.dev_cli_config["region"]} ' \
                  f'-c {self.dev_cli_config["commit"]} ' \
                  f'-a {self.dev_cli_config["autostop"]} ' \
                  f'--env {self.dev_cli_config["env"]}'
        print(command)

        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

    def edit_engine_name(self, new_engine_name=None, db_name=None, env=None):
        engine_name = new_engine_name or 'default_engine_' + self.dev_cli_config["env"]

        command = f'./dev-cli edit ' \
                  f'{db_name or self.dev_cli_config["database"]} ' \
                  f'-n {engine_name} ' \
                  f'--env {env or self.dev_cli_config["env"]}'
        print(command)

        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

    def stop_engine(self, engine_name=None, env=None):
        command = f'./dev-cli stop ' \
                  f'{engine_name or self.dev_cli_config["database"]} ' \
                  f'--env {env or self.dev_cli_config["env"]}'
        print(command)

        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()

    def start_engine(self, engine_name=None, env=None):
        command = f'./dev-cli start ' \
                  f'{engine_name or self.dev_cli_config["database"]} ' \
                  f'--env {env or self.dev_cli_config["env"]}'
        print(command)

        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()


class RestClient(ABC):

    def __init__(self, login=None, password=None, env='dev'):
        self.login = login
        self.password = password
        self.env = env
        self._session = requests.Session()

    @property
    def auth(self):
        return self.login, self.password

    def post(self,
             url: str,
             error_msg: str,
             data: dict = None,
             allow_redirects: bool = False,
             verify: bool = False,
             headers: dict = None,
             expected_status_codes: list = [],
             json_dumps: bool = True
             ):
        if json_dumps:
            data = json.dumps(data) or data
        response = self._session.post(url, data=data, headers=headers, allow_redirects=allow_redirects, verify=verify)

        if not response.ok and response.status_code not in expected_status_codes:
            raise Exception(f'{error_msg}. \n Response code: {response.status_code}, \n Response text: {response.text}')

        return response

    def get(self,
            url: str,
            error_msg: str,
            data: dict = None,
            allow_redirects: bool = False,
            verify: bool = False,
            headers: dict = None,
            expected_status_codes: list = []
            ):
        data = json.dumps(data) or data
        response = self._session.get(url, data=data, headers=headers, allow_redirects=allow_redirects, verify=verify)

        if not response.ok and response.status_code not in expected_status_codes:
            raise Exception(f'{error_msg}. \n Response code: {response.status_code}, \n Response text: {response.text}')

        return response


