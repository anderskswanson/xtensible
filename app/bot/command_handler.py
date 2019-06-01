import importlib
import os
import collections
from app.bot.message_parser import MessageParser
from app.bot.function_util import FunctionUtil


class CommandHandler:
    """
    Handle incoming commands
    Take command as input, delegate out to module, return data from module to 
    caller
    """

    MODULE_NF = '''Module {} could not be found. \
Check module exists on the host device'''

    def __init__(self, message_parser=MessageParser(),
                 function_getter=FunctionUtil()):
        self._modules = dict()
        self._message_parser = message_parser
        self._function_getter = function_getter

    # merge iterable of module names or string module name into the module dict
    def add_module(self, item):
        if not isinstance(item, collections.Iterable):
            self._modules[item] = None
        else:
            # merge module hashmaps
            new_modules = {key: None for key in item}
            self._modules = {**new_modules, **self._modules}
        # force reload of all modules
        self.load_modules()

    # add a module script into the module list
    def load_module(self, module):
        module_path = 'app/modules/{}.py'.format(module)
        import_string = 'app.modules.{}'.format(module)
        if not os.path.exists(os.path.join(module_path)):
            raise ModuleNotFoundError(self.MODULE_NF.format(module))
        key = importlib.import_module(import_string)
        self._modules[module] = key

    # load all module scripts into modules dict
    def load_modules(self):
        keys = list(self._modules.keys())
        for module in keys:
            try:
                self.load_module(module)
            except (ModuleNotFoundError):
                # replace with log message
                print(self.MODULE_NF.format(module))
                self._modules.pop(module)

    def __len__(self):
        return len(self._modules)

    def handle(self, tokens):
        return 'placeholder'
