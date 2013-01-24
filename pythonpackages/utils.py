from urllib import parse
from . import config


def get_query_string(request):
    """
    Return the parsed query string if it exists in the request.
    """
    qs = ''
    if 'QUERY_STRING' in request:
        qs = request['QUERY_STRING']
        qs = parse(qs)
    return qs


def get_logged_in():
    """
    Return a list of users that have signed in.
    """
    try:
        return config.REDIS.smembers('logged_in')
    except:
        # XXX No db
        return list()


def logged_out(user=None):
    """
    If user is None remove from list of signed in users.
    """
    if user is not None:
        config.REDIS.srem('logged_in', user)
        return


def set_logged_in(user):
    """
    Save signed in users to the database.
    """
    try:
        config.REDIS.sadd('logged_in', user)  # logged in users
        config.REDIS.sadd('site_users', user)  # all users ever
    except:
        pass
        # XXX No db
    return
