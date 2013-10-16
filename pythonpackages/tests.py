from pyramid import testing
import unittest


LOGGED_IN_ENTRY = "<a href='/aclark4life'>aclark4life</a> logged in 10/13/13"


class PythonPackagesTests(unittest.TestCase):
    def setUp(self):
        """
        """
        self.config = testing.setUp()

    def tearDown(self):
        """ Clear out the application registry """
        testing.tearDown()

    def test_root_view(self):
        from pythonpackages.views import root
        request = testing.DummyRequest()
        result = root(request)
        self.assertEqual(request.response.status, '200 OK')
        self.assertTrue('auth_url' in result)
        self.assertTrue('logged_in' in result)
        self.assertTrue('user' in result)
        self.assertEqual(request.response.headerlist[0],
                         ('Content-Type', 'text/html; charset=UTF-8'))

    def test_link_user(self):
        from pythonpackages.utils import link_user
        logged_in_entry = link_user('aclark4life logged in 10/13/13')
        assert logged_in_entry == LOGGED_IN_ENTRY
