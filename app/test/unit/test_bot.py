import unittest
from app.bot.bot import XtensibleBot
from app.bot.command_handler import CommandHandler


class FakeClient:
    def run(self, token):
        print('stated with token: {}'.format(token))


class TestBot(unittest.TestCase):
    def test_create_bot(self):
        test_bot = XtensibleBot('some_token', FakeClient(),
                                handler=CommandHandler())
        self.assertNotEqual(test_bot, None)


if __name__ == '__main__':
    unittest.main()
