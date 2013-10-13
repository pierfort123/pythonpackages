from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.security import forget
from pyramid.security import remember
try:  # Py3
    from urllib import parse as urlparse
except:  # Py2
    import urlparse


def about(request):
    return {}


def contact(request):
    return {}


def login(request):
    """
    """
    return {}

def logout(request):
    """
    """
    headers = forget(request)
    return HTTPFound(location="/", headers=headers)
