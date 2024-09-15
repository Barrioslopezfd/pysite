import unittest
from markdown_extraction import *


class TESTMarkdown_Extraction(unittest.TestCase):
    def test_extract_file(self):
        expected = "This a heading"
        got = extract_title("# This a heading\nThis is not a heading")

        self.assertEqual(expected, got)

    def test_extract_wrong_heading(self):
        expected = "This a heading"
        got = extract_title("## This a heading\nThis is not a heading")
        self.assertNotEqual(expected, got)
