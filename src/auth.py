import requests

from .utils import is_successful, print_response, urljoin


class Auth:
    _instance = None

    def __init__(self, sso_url, username, password):
        self.sso_url = sso_url
        self.username = username
        self.password = password
        self.token = ''
        self._login()
        __class__._instance = self

    @classmethod
    def instance(cls):
        if cls._instance:
            return cls._instance
        raise SystemExit('Please log in. You need to call Auth constructor')

    def jwt_header(self):
        return {'Authorization': f'JWT {self.token}'}

    def _login_url(self):
        return urljoin(self.sso_url, 'api/auth/login')

    def _payload(self):
        return {
            'username': self.username,
            'password': self.password,
        }

    def _login(self):
        url = self._login_url()
        response = requests.post(
            url=url,
            json=self._payload(),
        )

        if is_successful(response):
            self.token = response.json().get('access_token')
        else:
            print_response(response, url)
            raise SystemExit(-1)
