USER_LINK = "<a href='/%s'>%s</a> %s"


def link_user(logged_in_entry):
    parts = logged_in_entry.split()
    return USER_LINK % (parts[0], parts[0], ' '.join([parts[1], parts[2], parts[3]]))
