import unittest
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node=TextNode('This is a text node', text_type_bold)
        node2=TextNode('This is a text node', text_type_italic)
        self.assertNotEqual(node, node2)

    def test_eq_with_none(self):
        node =TextNode('This is a text node', text_type_bold, None)
        node2=TextNode('This is a text node', text_type_bold)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "google.com")
        self.assertEqual(
            "TextNode(This is a text node, text, google.com)", repr(node)
        )

        

if __name__ == "__main__":
    unittest.main()
