import os


_now = '%m/%d/%y'

GITHUB_CLIENT_ID = os.getenv('GITHUB_CLIENT_ID', '')
GITHUB_CLIENT_SECRET = os.getenv('GITHUB_CLIENT_SECRET', '')

client_id_pypi = os.getenv('PYPI_CONSUMER_KEY', '')
client_secret_pypi = os.getenv('PYPI_CONSUMER_SECRET', '')

auth_url_gh = 'https://github.com/login/oauth/authorize?client_id=%s' % (
    GITHUB_CLIENT_ID)

auth_url_pypi = (
    'https://pypi.python.org/oauth/authorise'
    '?oauth_token=%s&oauth_callback=http://pythonpackages.com/callback_pypi')

token_url_gh = 'https://github.com/login/oauth/access_token'
token_url_pypi = 'https://pypi.python.org/oauth/access_token'

user_url = 'https://api.github.com/user?%s'
