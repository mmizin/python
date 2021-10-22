from config import RestClient


class FireboltClient(RestClient):

    def __init__(self):
        super().__init__()

    def authenticate(self):
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        url = f'https://api.{self.env}.firebolt.io/auth/v1/login'
        data = {"username": "", "password": ""}

        response = self.post(url=url, data=data, headers=headers, error_msg='Authentication failed.')

        return response

    def get_engine(self):
        url = /engines/engine
