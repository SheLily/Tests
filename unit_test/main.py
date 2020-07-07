

import unittest
from yandex_translate import translate_it
#class Account_test(unittest.TestCase):
#    def setUp(self):
#        from accounting import *
#        
#    def test_documents(self):
#        self.assertEqual




class Yandex_test(unittest.TestCase):
    def setUp(self):
        self.translate_it = translate_it
        
    def test_en_hello(self):
        text, code = self.translate_it('hello')
        self.assertEqual('привет', text.lower())
        self.assertEqual(code, 200)
        
    def test_fr_hello(self):
        text, code = self.translate_it('bonjour')
        self.assertEqual('привет', text.lower())
        self.assertEqual(code, 200)
        
    def test_de_hello(self):
        text, code = self.translate_it('hallo')
        self.assertEqual('привет', text.lower())
        self.assertEqual(code, 200)
        
    def test_es_hello(self):
        text, code = self.translate_it('adiós')
        self.assertEqual('привет', text.lower())
        self.assertEqual(code, 200)
    
        
        

unittest.main()