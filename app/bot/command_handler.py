import importlib
import os
import collections
import inspect
from app.bot.message_parser import MessageParser
from app.bot.message_parser import MessageParserException
from app.bot.base import BaseModule


class CommandHandler:
    """
    Handle incoming commands
    Take command as input, delegate out to module, return data from module to 
    caller
    """

    # Error strings for caller, returned if running the command goes awry...
    HANDLER_ERR = 'Error parsing message {}\nMessage format: !<module> <func> [arguments...]'
    FUNC_NOT_FOUND_ERR = 'Function {} not found in module {}'
    MODULE_NF_ERR = 'Module {} not found'
    INVALID_ARGS_ERR = 'Invalid arguments supplied. Function {} signature: {}'
    EXEC_ERR = 'Error {} while executing function {}'

    def __init__(self, message_parser=MessageParser(),
                 base_module=BaseModule()):
        self._modules = dict()
        self._message_parser = message_parser
        self._base_module = base_module

    def _evaluate_message(self, parsed_message):
        output = ''
        # check module exists in loaded modules
        if parsed_message.module in self._base_module:
            module = self._base_module[parsed_message.module]
            # check function exists in module
            if hasattr(module, parsed_message.func):
                fn = getattr(module, parsed_message.func)
                # try to execute the function
                try:
                    output = fn(
                        *parsed_message.args,
                        **parsed_message.kwargs
                    )
                except TypeError:
                    signature = fn.__doc__
                    output = self.INVALID_ARGS_ERR.format(
                        fn.__name__,
                        signature
                    )
                except Exception as runtime_err:
                    output = self.EXEC_ERR.format(
                        runtime_err,
                        fn.__name__
                    )
            else:
                output = self.FUNC_NOT_FOUND_ERR.format(
                    parsed_message.func,
                    parsed_message.module)
        else:
            output = self.MODULE_NF_ERR.format(parsed_message.module)
        return output

    def handle(self, tokens):
        output = ''
        try:
            parsed_message = self._message_parser.parse_message(tokens)
            output = self._evaluate_message(parsed_message)
        except MessageParserException:
            if len(tokens) > 1 and tokens[0] not in self._base_module.keys():
                ouptut = self.MODULE_NF_ERR.format(tokens[0])
            else:
                output = self.HANDLER_ERR.format(tokens)
        return output
