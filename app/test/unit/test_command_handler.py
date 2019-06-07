import unittest
from app.bot.command_handler import CommandHandler
from app.bot.message_parser import MessageParser
from app.bot.message_parser import MessageParserException

RAISE_ERR = 'ok'


class FakeMessageParser:
    def parse_message(self, message):
        if message != RAISE_ERR:
            return MessageParser.ParsedMessage(*message.split(' '), dict())
        else:
            raise MessageParserException('bad message')


class FakeBaseModule:
    def __init__(self):
        self._modules = {'list': list()}

    def __getitem__(self, item):
        return self._modules[item]

    def __contains__(self, item):
        return item in self._modules

    def __len__(self):
        return len(self._modules)


class TestCommandHandler(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.command_handler = CommandHandler(
            message_parser=FakeMessageParser(),
            base_module=FakeBaseModule()
        )

    @classmethod
    def tearDown(self):
        self.command_handler = None

    def test_function_not_found(self):
        # should return a function not found message
        msg = self.command_handler._message_parser.parse_message('list foo bar')
        out = self.command_handler._evaluate_message(msg)
        self.assertEqual(self.command_handler.FUNC_NOT_FOUND_ERR.format('foo', 'list'), out)

    def test_module_not_found(self):
        msg = self.command_handler._message_parser.parse_message('foo bar bat')
        out = self.command_handler._evaluate_message(msg)
        self.assertEqual(self.command_handler.MODULE_NF_ERR.format('foo'), out)

    def test_invalid_args(self):
        msg = self.command_handler._message_parser.parse_message('list append baz')
        out = self.command_handler._evaluate_message(msg)
        expected = self.command_handler.INVALID_ARGS_ERR.format(list.append.__name__, list.append.__doc__)
        self.assertEqual(expected, out)