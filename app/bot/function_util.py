
class FunctionUtil:

    def get_function(self, module, name):
        try:
            return getattr(module, name)
        except (AttributeError):
            return None
