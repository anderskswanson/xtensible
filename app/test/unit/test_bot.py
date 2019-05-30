import unittest
from ...bot.bot import XtensibleBot


class FakeClient:
    def run(self, token):
        print('stated with token: {}'.format(token))


class TestBot(unittest.TestCase):
    def test_create_bot(self):
        test_bot = XtensibleBot('some_token', FakeClient())
        self.assertNotEquals(test_bot, None)

if __name__ == '__main__':
    unittest.main()
