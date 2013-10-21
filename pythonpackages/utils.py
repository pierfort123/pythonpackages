from pyramid.security import unauthenticated_userid


LINK_USER = "<a href='/%s'>%s</a> %s"


def get_user(request):
    """
    """
    import pdb ; pdb.set_trace()
    userid = authenticated_userid(request)
    if userid in [i.decode() for i in db.smembers('users')]:
        return userid
    return None


def link_user(logged_in_entry):
    """
    Take a string e.g. `aclark4life logged in 10/13/13` and return
    `<a href="/aclark4life">aclark4life</a> logged in 10/13/13`
    """
    parts = logged_in_entry.split()
    return LINK_USER % (
        parts[0], parts[0], ' '.join([parts[1], parts[2], parts[3]]))
