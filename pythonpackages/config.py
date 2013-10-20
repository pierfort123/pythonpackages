import os

API_GH_USER = 'https://api.github.com/user?%s'

FORMAT = '%m/%d/%y'

GH_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', '')
GH_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', '')

GH_AUTH_URL = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GH_CLIENT_ID)

GH_TOKEN_URL = 'https://github.com/login/oauth/access_token'

PYPI_TOKEN_URL = 'https://pypi.python.org/oauth/access_token'
