from flask_testing import TestCase

from backend.app import create_app


class AppTestCase(TestCase):

    def create_app(self):
        return create_app('testing')
