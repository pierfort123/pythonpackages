import os

user_url = 'https://api.github.com/user?%s'

_now = '%m/%d/%y'

GH_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', '')
GH_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', '')

auth_url = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GH_CLIENT_ID)

GH_TOKEN_URL = 'https://github.com/login/oauth/access_token'

PYPI_TOKEN_URL = 'https://pypi.python.org/oauth/access_token'
