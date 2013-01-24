import os


GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID', None)
GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET', None)
GITHUB_SCOPE = ''  # http://developer.github.com/v3/oauth/#scopes
GITHUB_URL = 'https://github.com'
GITHUB_URL_API = 'https://api.github.com'
GITHUB_URL_AUTH = (GITHUB_URL + '/login/oauth/authorize?client_id=%s&scope=%s'
    % (GITHUB_CLIENT_ID, GITHUB_SCOPE))
#REDIS_KEY_USER_PLAN
#REDIS_KEY_USER_PYPI_OAUTH_TOKEN
#REDIS_KEY_USER_PYPI_OAUTH_SECRET
#REDIS_KEY_USER_PYPI_OAUTH_SECRET
#REDIS_KEY_USER_PYPI_OAUTH_TOKEN
PYPI_OAUTH_CONSUMER_KEY = os.environ.get('PYPI_OAUTH_CONSUMER_KEY', None)
PYPI_OAUTH_CONSUMER_SECRET = os.environ.get('PYPI_OAUTH_CONSUMER_SECRET', None)
