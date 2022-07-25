import unittest

from translator import english_to_french, french_to_english

class test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french(" "), "Bonjour") 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertNotEqual(english_to_french("Hello"), "Au revoir")  

class test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english(" "), "Hello")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Au revoir"), "Hello")  

unittest.main()