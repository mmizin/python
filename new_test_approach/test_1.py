import pytest


class New_1_Test:

    def test_1(self, dev_cli, fb_api):
        print('\nHERE test_1')
        auth_data = fb_api.authenticate()
        print(f'AUTH {auth_data.json()}')

    def test_2(self):
        print('\nHERE test_2')


