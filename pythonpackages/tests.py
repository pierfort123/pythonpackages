import unittest
from pyramid import testing

class TestPythonPackages(unittest.TestCase):
    def setUp(self):
        request = testing.DummyRequest()
        self.config = testing.setUp(request=request)

    def tearDown(self):
        testing.tearDown()

    def test_something(self):
        assert True
