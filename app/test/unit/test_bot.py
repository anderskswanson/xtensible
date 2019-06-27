import unittest
from app.bot.bot import XtensibleBot
from app.bot.command_handler import CommandHandler


class FakeClient:
    def run(self, token):
        print('stated with token: {}'.format(token))

    def event(self, arg):
        pass

    def send_message(self, arg1, arg2):
        pass


class FakeHandler:
    def handle(self, *args, **kwargs):
        return 'foo'


class TestBot(unittest.TestCase):  
    @classmethod
    def setUp(self):
        self.bot = XtensibleBot('foo', FakeClient(), FakeHandler())

    def test_run(self):
        self.bot.run()

if __name__ == '__main__':
    unittest.main()
