import unittest
from app.bot.command_handler import CommandHandler


class TestCommandHandler(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.command_handler = CommandHandler()

    @classmethod
    def tearDown(self):
        self.command_handler = None
