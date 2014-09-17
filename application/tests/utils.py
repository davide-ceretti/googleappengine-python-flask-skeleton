import unittest

from google.appengine.ext import testbed

from application import app


class NDBTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create your Flask app here, with any
        configuration you need
        """
        return app

    def __call__(self, result=None):
        """
        Does the required setup, doing it here
        means you don't have to call super.setUp
        in subclasses.
        """
        self._pre_setup()
        super(NDBTestCase, self).__call__(result)
        self._post_tearDown()

    def _pre_setup(self):
        self.app = self.create_app()
        self.client = self.app.test_client()

        self.testbed = testbed.Testbed()
        self.testbed.activate()

        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

        # now you can use flask thread locals

        self._ctx = self.app.test_request_context()
        self._ctx.push()

    def _post_tearDown(self):
        self._ctx.pop()

        self.testbed.deactivate()
