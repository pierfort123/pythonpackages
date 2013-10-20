import os

user_url = 'https://api.github.com/user?%s'

_now = '%m/%d/%y'

client_id = os.getenv('GITHUB_CLIENT_ID', '')
client_secret = os.getenv('GITHUB_CLIENT_SECRET', '')

auth_url = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    client_id)

token_url_gh = 'https://github.com/login/oauth/access_token'

token_url_pypi = 'https://pypi.python.org/oauth/access_token'
