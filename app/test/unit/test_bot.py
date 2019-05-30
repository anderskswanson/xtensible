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
        self.assertNotEquals(test_bot, None)

    def test_parse_message(self):
        test_bot = XtensibleBot('some_token', FakeClient(),
                                handler=CommandHandler())

        # it should only parse commands beginning with '!'
        msg = test_bot._parse_message('blah')
        self.assertEquals(msg, None)

        # it should parse commands into lists, splitting on ' '
        msg = test_bot._parse_message('!foo bar')
        self.assertEqual(msg[0], 'foo')
        self.assertEqual(msg[1], 'bar')


if __name__ == '__main__':
    unittest.main()
