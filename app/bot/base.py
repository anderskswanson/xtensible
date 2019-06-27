from inspect import getmembers
import importlib
import os


class BaseModule:
    """
    Module of native features for XtensibleBot
    Available functions:
    - lsmod
    - describemod
    - addmod
    - delmod
    - help
    """

    _NOT_LOADED = 'Module {} is not loaded into Xtensible-Bot'

    def __init__(self):
        self._modules = {'base': self}
        static_modules = [os.path.basename(item.path)
                          for item in os.scandir("app/modules")
                          if item.is_dir() and '__pycache__' not in item.path]
        for mod in static_modules:
            self._load_module(mod)

    def __len__(self):
        return len(self._modules)

    def __getitem__(self, key):
        return self._modules[key]

    def __setitem__(self, key, value):
        self._modules[key] = value

    def __contains__(self, key):
        return key in self._modules

    def __delitem__(self, key):
        self._modules.pop(key)

    # add a module script into the module list
    def _load_module(self, module):
        module_path = 'app/modules/{}/module_exports.py'.format(module)
        import_string = 'app.modules.{}.module_exports'.format(module)
        if not os.path.exists(os.path.join(module_path)):
            raise ModuleNotFoundError(self._NOT_LOADED.format(module))
        key = importlib.import_module(import_string)
        self[module] = key

    def keys(self):
        """
        Internal representation of lsmod
        !base keys
        """
        return self._modules.keys()

    # merge iterable of module names or string module name into the module dict
    def addmod(self, item):
        """
        Add module/s from the modules directory into the Xtensible-Bot
        !base addmod <module1 module2 ...>
        """
        loaded_modules = []
        failed_loads = []
        if not isinstance(item, list):
            item = [item]
        # merge module hashmaps
        for name in item:
            try:
                module_obj = self._load_module(name)
                self[name] = module_obj
                loaded_modules.append(name)
            except ModuleNotFoundError:
                failed_loads.append(name)
        return loaded_modules, failed_loads

    def lsmod(self):
        """
        List all modules loaded into the Xtensible-Bot
        !base lsmod
        """
        return 'Loaded Modules:\n{}'.format(
            '\n'.join([module for module in self._modules]))

    def delmod(self, module):
        """
        Delete (unload) a module from the Xtensible-Bot
        !base delmod <module>
        """
        if module in self:
            del self[module]
            return 'Removed module {}'.format(module)
        else:
            return self._NOT_LOADED.format(module)

    def describemod(self, module):
        """
        Return a description of each member function of a module
        !base describemod module
        """
        if module in self:
            attrs = getmembers(self[module])
            methods = ['{}: {}'.format(attr[0], attr[1].__doc__) 
                        for attr in attrs if not attr[0].startswith('_')]
            return '\n'.join(methods)
        else:
            return self._NOT_LOADED.format(module)
