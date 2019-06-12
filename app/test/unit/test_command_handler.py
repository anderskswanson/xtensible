import unittest
from app.bot.command_handler import CommandHandler
from app.bot.message_parser import MessageParser
from app.bot.message_parser import MessageParserException

RAISE_ERR = 'ok'


class FakeMessageParser:
    def parse_message(self, message):
        if message != RAISE_ERR:
            args = message.split(' ')
            if len(args) < 3:
                return MessageParser.ParsedMessage(*args, list(), dict())
            else:
                mod = args[0]
                fn = args[1]
                args = args[2:]
                return MessageParser.ParsedMessage(mod, fn, args, dict())
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

    def keys(self):
        return self._modules.keys()


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
        msg = self.command_handler._message_parser.parse_message('list append')
        out = self.command_handler._evaluate_message(msg)
        expected = self.command_handler.INVALID_ARGS_ERR.format(list.append.__name__, list.append.__doc__)
        self.assertEqual(expected, out)

    def test_runtime_err(self):
        err = 'pop from empty list'
        expected = self.command_handler.EXEC_ERR.format(
            err,
            'pop'
        )
        msg = self.command_handler._message_parser.parse_message('list pop')
        out = self.command_handler._evaluate_message(msg)
        self.assertEqual(expected, out)

    def test_run_cmd(self):
        # module objects should maintain state
        msg1 = self.command_handler._message_parser.parse_message('list append hello')
        msg2 = self.command_handler._message_parser.parse_message('list pop')
        out = self.command_handler._evaluate_message(msg1)
        out = self.command_handler._evaluate_message(msg2)
        self.assertEqual('hello', out)

    def test_handle_module_nf(self):
        self.command_handler._message_parser = MessageParser()
        out = self.command_handler.handle('!baz foo bar')
        self.assertEqual(
            self.command_handler.MODULE_NF_ERR.format('baz'),
            out
        )

    def test_handle_msg_err(self):
        self.command_handler._message_parser = MessageParser()
        out = self.command_handler.handle('!')
        expected = self.command_handler.HANDLER_ERR.format('!')
        self.assertEqual(expected, out)

    def test_handle_cmd(self):
        self.command_handler._message_parser = MessageParser()
        out = self.command_handler.handle('!list append hello')
        out = self.command_handler.handle('!list pop')
        self.assertEqual('hello', out)