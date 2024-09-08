import unittest
from block_markdown import *


class TESTBlockMarkdown(unittest.TestCase):

    def test_block_markdown(self):
        document = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item 
"""

        what_i_want = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]

        what_i_have = markdown_to_blocks(document)

        self.assertListEqual(what_i_want, what_i_have)

    def test_block_type(self):
        what_i_have = []
        text = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
            "1. primer item\n2. segundo item\n3. tercer item",
        ]
        for t in text:
            what_i_have.append(block_to_block_type(t))

        what_i_want = ["heading", "paragraph", "unordered_list", "ordered_list"]

        self.assertListEqual(what_i_have, what_i_want)

    def test_individual_block(self):
        my_block = "# This is a heading"
        actual_block = block_to_block_type(my_block)
        self.assertEqual(actual_block, "heading")
