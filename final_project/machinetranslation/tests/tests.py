import unittest
import translator
class TestNullInputs(unittest.TestCase):
    def test_null_input_for_french_to_english(self):
        with self.assertRaises(ValueError):
            translator.french_to_english(None)

    def test_null_input_for_english_to_french(self):
        with self.assertRaises(ValueError):
            translator.english_to_french(None)

class TestTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour', 'Translation does not match')

    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello', 'Translation does not match')