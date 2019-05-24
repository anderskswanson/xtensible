from discord import Client


class XtensibleBot:
    """
    Modular discord bot
    """
    def __init__(self, access_token, modules=list(), client=Client()):
        self._access_token = access_token
        self._modules = modules
        self._client = client

    def run(self):
        self._client.run(self._access_token)

    class CommandHandler:
        """
        Handler for incoming commands to the bot
        """
        def __init__(self):
            raise NotImplementedError()
