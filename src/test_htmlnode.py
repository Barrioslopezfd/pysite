import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node=LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_children_no_prop(self):
        node=LeafNode("p", "This is a paragraph of text.", {})
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_with_props(self):
        node=LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_no_tag(self):
        node=LeafNode(None, 'This is a none tagged test', None)
        self.assertEqual(node.to_html(), 'This is a none tagged test')
    
    def test_no_prop_parent(self):
        node = ParentNode( "p",[
            LeafNode("b", "Bold text", None),
            LeafNode(None, "Normal text", None),
            LeafNode("i", "italic text", None),
            LeafNode(None, "Normal text", None)],
            None)
        self.assertEqual(node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_prop_parent(self):
        node = ParentNode( "p",[
            LeafNode("b", "Bold text", None),
            LeafNode(None, "Normal text", None),
            LeafNode("i", "italic text", None),
            LeafNode(None, "Normal text", None)],
            {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<p href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
if __name__ == "__main__":
    unittest.main()
