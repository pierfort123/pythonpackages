from pyramid import testing
import unittest


class ViewIntegrationTests(unittest.TestCase):
    def setUp(self):
        """
        """
        self.config = testing.setUp()

    def tearDown(self):
        """ Clear out the application registry """
        testing.tearDown()

    def test_root(self):
        from pythonpackages.views import root
        request = testing.DummyRequest()
        result = root(request)
        self.assertEqual(request.response.status, '200 OK')
        self.assertTrue('auth_url' in result)
        self.assertTrue('logged_in' in result)
        self.assertTrue('user' in result)
        self.assertEqual(request.response.headerlist[0],
                         ('Content-Type', 'text/html; charset=UTF-8'))
