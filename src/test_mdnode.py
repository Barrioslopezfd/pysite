from mdnode import split_nodes_delimiter
from textnode import *
import unittest

class TestMDNode(unittest.TestCase):
    def test_splitter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        self.assertEqual(new_nodes, [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text),])

    def test_end_with_delimiter(self):
        node = TextNode("This is text that ends with a `delimiter`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)

        self.assertEqual(new_nodes, [TextNode("This is text that ends with a ", text_type_text), TextNode("delimiter", text_type_code),])
