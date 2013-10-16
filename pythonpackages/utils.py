LINK_USER = "<a href='/%s'>%s</a> %s"


def link_user(logged_in_entry):
    """
    Takes a string e.g. `aclark4life logged in 10/13/13` and returns
    `<a href="/aclark4life">aclark4life</a> logged in 10/13/13`
    """
    parts = logged_in_entry.split()
    return LINK_USER % (parts[0], parts[0], ' '.join([parts[1], parts[2], parts[3]]))
