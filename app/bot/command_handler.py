import importlib
import os
import collections
from app.bot.message_parser import MessageParser
from app.bot.message_parser import MessageParserException
from app.bot.base import BaseModule


class CommandHandler:
    """
    Handle incoming commands
    Take command as input, delegate out to module, return data from module to 
    caller
    """

    HANDLER_ERR = 'Error parsing message {}\nMessage format: !<module> <func> [arguments...]'
    FUNC_NOT_FOUND_ERR = 'Function {} not found in module {}'
    MODULE_NF_ERR = 'Module {} not found'

    def __init__(self, message_parser=MessageParser(),
                 base_module=BaseModule()):
        self._modules = dict()
        self._message_parser = message_parser
        self._base_module = base_module

    def _get_function(self, module, name):
        if hasattr(module, name):
            obj = getattr(module, name)
        else:
            return None

    def handle(self, tokens):
        output = ''
        try:
            parsed_message = self._message_parser.parse_message(tokens)
            module = self._base_module[parsed_message.module]
            func = self._get_function(module, parsed_message.func)
            if func is None:
                output = self.FUNC_NOT_FOUND_ERR.format(parsed_message.func)
            else:
                args = parsed_message.args
                kwargs = parsed_message.kwargs
                output = func(*args, **kwargs)
        except MessageParserException:
            if len(tokens) > 1 and tokens[0] not in self._base_module.keys():
                ouptut = self.MODULE_NF_ERR.format(tokens[0])
            else:
                output = self.HANDLER_ERR
        return output
