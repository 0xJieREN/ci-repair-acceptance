import unittest

from calc.text import slugify


class SlugifyTests(unittest.TestCase):
    def test_mixed_case_words(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_punctuation_is_dropped(self):
        self.assertEqual(slugify("CI: Repair, Now!"), "ci-repair-now")
