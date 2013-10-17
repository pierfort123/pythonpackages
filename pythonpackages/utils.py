from pyramid.security import unauthenticated_userid
from .db import db


LINK_USER = "<a href='/%s'>%s</a> %s"


# Via http://docs.pylonsproject.org/projects/pyramid_cookbook/\
# en/latest/auth/user_object.html
def get_user(request):
    """
    """
    user = unauthenticated_userid(request)
    if user is not None:
        if user in [i.decode() for i in db.smembers('users')]:
            return user
        else:
            return None


def link_user(logged_in_entry):
    """
    Take a string e.g. `aclark4life logged in 10/13/13` and return
    `<a href="/aclark4life">aclark4life</a> logged in 10/13/13`
    """
    parts = logged_in_entry.split()
    return LINK_USER % (
        parts[0], parts[0], ' '.join([parts[1], parts[2], parts[3]]))
