import unittest
from app.bot.message_parser import MessageParser
from app.bot.message_parser import MessageParserException


class TestMessageParser(unittest.TestCase):

    MSG = '!foo bar arg1 arg2 arg3=3 arg4=4 arg5'
    TOKENS = ['foo', 'bar', 'arg1', 'arg2', 'arg3=3', 'arg4=4', 'arg5']
    ARGS = ['arg1', 'arg2', 'arg5']
    KWARGS = {'arg3': '3', 'arg4': '4'}
    PARSED_MSG = MessageParser.ParsedMessage(
        'foo',
        'bar',
        ARGS,
        KWARGS
    )

    @classmethod
    def setUpClass(self):
        self.message_parser = MessageParser()

    # the "_get_x" functions always expect a preprocessed list of message
    # tokens

    def test_get_func(self):
        self.assertEqual('bar', self.message_parser._get_func(self.TOKENS))
        self.assertNotEqual('foo', self.message_parser._get_func(self.TOKENS))

    def test_get_module(self):
        self.assertEqual('foo', self.message_parser._get_module(self.TOKENS))
        self.assertNotEqual(
            'bar',
            self.message_parser._get_module(self.TOKENS)
        )

    def test_get_args(self):
        self.assertEqual(
            self.ARGS,
            self.message_parser._get_args(self.TOKENS[2:])
        )

    def test_get_kwargs(self):
        self.assertEqual(
            self.KWARGS,
            self.message_parser._get_kwargs(self.TOKENS[2:])
        )

    def test_get_tokens(self):
        self.assertEqual(
            self.TOKENS,
            self.message_parser._get_tokens(self.MSG)
        )
        self.assertIsNone(None, self.message_parser._get_tokens(''))
        self.assertIsNone(self.message_parser._get_tokens('foo bar baz'))

    def test_parse_message(self):
        parsed_message = self.message_parser.parse_message(self.MSG)
        self.assertEqual(self.PARSED_MSG, parsed_message)
        try:
            self.message_parser.parse_message('')
        except MessageParserException:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised', e)
        else:
            self.fail('Expected exception MessageParserException')

if __name__ == '__main__':
    unittest.main()
