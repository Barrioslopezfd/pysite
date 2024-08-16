import unittest
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node=TextNode('This is a text node', 'bold')
        node2=TextNode('This is a text node', 'italic')
        self.assertNotEqual(node, node2)

    def test_eq_with_none(self):
        node =TextNode('This is a text node', 'bold', None)
        node2=TextNode('This is a text node', 'bold')
        self.assertEqual(node, node2)

        

if __name__ == "__main__":
    unittest.main()
