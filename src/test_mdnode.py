import unittest
from mdnode import *
from textnode import *


class TestMDNode(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_bold_bold(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_2bold_3bold(self):
        node = TextNode(
            "This text contains this **bolded word** and this **other bolded word**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This text contains this ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and this ", text_type_text),
                TextNode("other bolded word", text_type_bold),
            ],
            new_nodes,
        )

    def test_4bold_1bold(self):
        node = TextNode(
            "This is text with a **very very bolded word** and **this**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("very very bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("this", text_type_bold),
            ],
            new_nodes,
        )

    def test__bold_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
