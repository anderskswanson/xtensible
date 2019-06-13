import unittest
from app.bot.base import BaseModule


class TestBase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base = BaseModule()

    @classmethod
    def tearDown(self):
        self.base = None

    def test_keys(self):
        expected = {'base': ''}.keys()
        self.assertEqual(expected, self.base.keys())

    def test_describemod(self):
        out = self.base.describemod('base')
        funcs = 'addmod delmod lsmod load_modules describemod'.split()
        for func in funcs:
            self.assertTrue(func in out)

    def test_describemod_nf(self):
        out = self.base.describemod('foo')
        expected = self.base._NOT_LOADED.format('foo')
        self.assertEqual(expected, out)

    def test_lsmod(self):
        out = self.base.lsmod()
        self.assertTrue('base' in out)

    def test_delmod(self):
        self.assertTrue(len(self.base) == 1)
        out = self.base.delmod('base')
        self.assertTrue(len(self.base) == 0)
        self.assertTrue('base' in out)
    
    def test_delmod_nf(self):
        out = self.base.delmod('foo')
        expected = self.base._NOT_LOADED.format('foo')
        self.assertEqual(expected, out)
