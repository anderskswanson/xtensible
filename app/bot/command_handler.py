import importlib
import os
import collections


class CommandHandler():

    MODULE_NF = '''Module {} could not be found. \
Check module exists on the host device'''

    def __init__(self):
        self._modules = dict()

    # merge iterable of module names or string module name into the module dict
    def add_module(self, item):
        if not isinstance(item, collections.Iterable):
            self._modules[item] = None
        else:
            new_modules = {key: None for key in item}
            self._modules = {**new_modules, **item}
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
        for module in self._modules.keys:
            try:
                self.load_module(module)
            except ModuleNotFoundError err:
                # replace with log message
                print(self.MODULE_NF.format(module))
                self._modules.pop(module)

    def __len__(self):
        return len(self._modules)

    def handle(self, tokens):
        return 'hello, world'
