from pprint import pprint

from config import RestClient
from firebolt.client import client
from firebolt.common import settings
from firebolt.db import connection
from firebolt.model import database
from firebolt.model import engine


class FireboltClient(RestClient):

    account_ids = {'dev': '{ACCOUNT_ID}',
                   'staging': '{ACCOUNT_ID}'}

    HEADER = {"Content-Type": "application/json;charset=UTF-8"}
    AUTH_HEADER = {"Authorization": "Bearer {}"}

    API_RUN_QUERY = 'https://{}/?database={}'

    def __init__(self):
        super().__init__()
        self.api_url = f'https://api.{self.env}.firebolt.io'

    def authenticate(self):
        url = self.api_url + '/auth/v1/login'
        data = {"username": "{EMAIL}", "password": "{PASSWORD}"}

        return self.post(url=url, data=data, headers=self.HEADER, error_msg='Authentication failed.')

    def get_engine_url(self, engine_name, access_token):
        url = self.api_url + f'/core/v1/accounts/{self.account_ids[self.env]}/engines?filter.name_contains={engine_name}'
        headers = {"Authorization": f"Bearer {access_token}"}

        return self.get(url, headers=headers, error_msg='GET_ENGINE_URL_FAILED').json()['edges'][0]['node']['endpoint']

    def execute_query(self, engine_url, db_name, query, access_token):
        url = 'https://{}/?database={}'.format(engine_url, db_name)
        headers = {"Authorization": f"Bearer {access_token}"}

        return self.post(url, data=query, headers=headers, error_msg='EXECUTE_QUERY_FAILED', json_dumps=False)




