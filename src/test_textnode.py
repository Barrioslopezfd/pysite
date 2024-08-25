import unittest

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
    def test_link_to_html(self):
        node = TextNode("This a link node", text_type_link, "google.com")
        self.assertEqual(node.text_node_to_html_node(), '<a href="google.com">This a link node</a>')
        
    def test_img_to_html(self):
        node = TextNode("This an img node", text_type_image, "google.com")
        self.assertNotEqual(node.text_node_to_html_node(), '<img src="google.com" alt="This and img node"></img>')

if __name__ == "__main__":
    unittest.main()
