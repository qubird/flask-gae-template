from flask.ext.testing import TestCase

from web import app


class MockResponse(object):
    def __init__(self, content, status_code=200):
        self.status_code = status_code
        self.content = content


class TestCase(TestCase):
    def create_app(self):
        app.TESTING = True
        return app

    def assert_flashes(self, expected_message, expected_category='message'):
        with self.client.session_transaction() as session:
            try:
                category, message = session['_flashes'][-1]
            except KeyError:
                raise AssertionError('nothing flashed')
            assert expected_message in message
            assert expected_category == category
