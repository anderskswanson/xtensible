from discord import Client
from app.bot.command_handler import CommandHandler


class XtensibleBot:
    """
    Modular discord bot
    """
    def __init__(self, access_token, modules=list(), client=Client(),
                 handler=CommandHandler()):
        self._access_token = access_token
        self._modules = modules
        self._client = client
        self._handler = handler

        # point client events to bot methods
        client.event(self.on_ready)
        client.event(self.on_message)

    def run(self):
        self._client.run(self._access_token)

    async def on_ready(self):
        print('Started XtensibleBot')

    async def on_message(self, message):
        output = self._handler.handle(message.content)
        await self._client.send_message(
            message.channel,
            output
        )

        if tokens is not None:
            output = self._handler.handle(tokens)
            await self._client.send_message(
                message.channel,
                output
            )
