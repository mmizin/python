from pprint import pprint

import pytest


class New_1_Test:

    def test_1(self, dev_cli, fb_api):
        print('\nHERE test_1')
        auth_data = fb_api.authenticate()
        # print(f'AUTH {auth_data.json()}')
        access_token = auth_data.json()['access_token']
        engine_url = fb_api.get_engine_url(engine_name='mmizin_DB_engine_1', access_token=access_token)
        # print(engine_url)
        res = fb_api.execute_query(engine_url, query="show cache", db_name='mmizin_DB', access_token=access_token)
        # pprint(res.json())

    def test_2(self):
        print('\nHERE test_2')


