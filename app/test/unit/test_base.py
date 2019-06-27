import unittest
from app.bot.base import BaseModule


class TestBase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base = BaseModule()

    @classmethod
    def tearDown(self):
        self.base = None

    def test_static_module_loaded(self):
        self.assertTrue('util' in self.base)

    def test_load_module(self):
        self.base._modules = dict()
        self.base._load_module('util')
        self.assertTrue('util' in self.base)

    def test_module_nf(self):
        try:
            self.base._load_module('invalid module')
        except ModuleNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raise', e)
        else:
            self.fail('Expected exception {}', ModuleNotFoundError.__name__)

    def test_addmod(self):
        self.base._modules = dict()
        rv = self.base.addmod('util')
        self.assertTrue('util' in self.base)
        self.assertEqual((['util'], []), rv)

    def test_add_two_modules(self):
        self.base_modules = dict()
        rv = self.base.addmod(['util', 'not a mod'])
        self.assertEqual((['util'], ['not a mod']), rv)

    def test_keys(self):
        self.base._modules = dict()
        self.base.addmod('util')
        expected = {'util': ''}.keys()
        self.assertEqual(expected, self.base.keys())

    def test_describemod(self):
        out = self.base.describemod('base')
        funcs = 'addmod delmod lsmod describemod'.split()
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
        self.base._modules = dict()
        self.base._load_module('util')
        self.assertTrue(len(self.base) == 1)
        out = self.base.delmod('util')
        self.assertTrue(len(self.base) == 0)
        self.assertTrue('util' in out)
    
    def test_delmod_nf(self):
        out = self.base.delmod('foo')
        expected = self.base._NOT_LOADED.format('foo')
        self.assertEqual(expected, out)
