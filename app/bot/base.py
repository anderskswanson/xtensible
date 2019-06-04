
class BaseModule: 
    """
    Module of native features for XtensibleBot
    Available functions:
    - listmod
    - describemod
    - addmod
    - delmod
    - help
    """

    def __init__(self):
        self._modules = dict()
    
    # merge iterable of module names or string module name into the module dict
    def add_module(self, item):
        if not isinstance(item, collections.Iterable):
            item = [item]
        else:
            # merge module hashmaps
            new_modules = {key: None for key in item}
            self._modules = {**new_modules, **self._modules}
        # force reload of all modules
        self.load_modules()

    # add a module script into the module list
    def load_module(self, module):
        module_path = 'app/modules/{}/module_exports.py'.format(module)
        import_string = 'app.modules.{}.module_exports'.format(module)
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
            except ModuleNotFoundError:
                # replace with log message
                print(self.MODULE_NF.format(module))
                self._modules.pop(module)

    def __len__(self):
        return len(self._modules)

    def __getitem__(self, key):
        return self._modules[key]

    def __delitem__(self, key):
        self._modules.pop(key)

    def keys(self):
        return list(self.keys())

    def listmod(self, module):
        """
        list all modules loaded into the Xtensible Bot
        """
        return 'Available Modules:\n{}'.format(
            '\n'.join([module for module in self._modules]))
