
class MessageParserException(Exception):

    def __init__(self, message):
        super().__init__(message)


class MessageParser:
    """
    Parse message into 4 components:
        - module
        - func
        - args (optional)
        - kwargs (optional)
    """
    class ParsedMessage:
        """
        Message containing data about a module, function, and its args
        """
        def __init__(self, module, func, args, kwargs):
            self.module = module
            self.func = func
            self.args = args
            self.kwargs = kwargs

        def __eq__(self, other):
            if other is None:
                return False
            if isinstance(other, MessageParser.ParsedMessage):
                return self.module == other.module and \
                    self.func == other.func and \
                    self.args == other.args and \
                    self.kwargs == other.kwargs
            else:
                return NotImplemented

        def __hash__(self):
            return hash(self.module, self.func, self.args, self.kwargs)
        
    TOKEN_ERR = 'Cannot parse a message with less than two tokens'

    def _get_module(self, message):
        return message[0]

    def _get_func(self, message):
        return message[1]

    def _get_args(self, message):
        return [arg for arg in message if '=' not in arg]

    def _get_kwargs(self, message):
        kwargs = [kwarg.split('=') for kwarg in message if '=' in kwarg]
        kwargs = {kwarg[0]: kwarg[1] for kwarg in kwargs if len(kwarg) == 2}
        return kwargs

    def _get_tokens(self, message):
        if message is None:
            return message
        if len(message) < 1:
            return None
        if message[0] != '!':
            return None
        return message[1:].split(' ')

    # return parsed message data
    # throws MessageParserException if the message does not have fields for
    # module or func
    def parse_message(self, message):
        module, func, args, kwargs = [None] * 4
        tokens = self._get_tokens(message)
        if tokens is None or len(tokens) < 2:
            raise MessageParserException(self.TOKEN_ERR)
        module = self._get_module(tokens)
        func = self._get_func(tokens)
        args = self._get_args(tokens[2:])
        kwargs = self._get_kwargs(tokens[2:])

        return self.ParsedMessage(module, func, args, kwargs)
