import unittest
from inline_markdown import *
from textnode import *


class TestMDNode(unittest.TestCase):
    def test_bold(self):
        node = [
            TextNode("**This like Tolkien**. with a **bolded** word", text_type_text)
        ]
        new_nodes = split_nodes_delimiter(node, "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This like Tolkien", text_type_bold),
                TextNode(". with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_bolded_tolkien(self):
        node = [
            TextNode(
                "**I like Tolkien**. read my [first post here](/majesty) (sorry the link doesn't work yet)",
                text_type_text,
            )
        ]
        new_nodes = split_nodes_delimiter(node, "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("I like Tolkien", text_type_bold),
                TextNode(
                    ". read my [first post here](/majesty) (sorry the link doesn't work yet)",
                    text_type_text,
                ),
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
            "This text contains this **bolded word** and this **other bolded word**",
            text_type_text,
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

    def test_bold_italic(self):
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

    def test_img_img(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        cosa = extract_markdown_images(text)
        res = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(cosa, res)

    def test_link_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        cosa = extract_markdown_links(text)
        res = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(cosa, res)

    def test_img_link1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        cosa = extract_markdown_images(text)
        res = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(cosa, res)

    def test_img_link2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)"
        cosa = extract_markdown_links(text)
        res = [("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(cosa, res)

    def test_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", text_type_text),
                TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode(
                    "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
                ),
            ],
        )

    def test_img(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode(
                    "rick roll", text_type_image, "https://i.imgur.com/aKaOqIh.gif"
                ),
                TextNode(" and ", text_type_text),
                TextNode(
                    "obi wan", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"
                ),
            ],
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        what_i_want = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode(
                "obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]

        what_i_have = text_to_textnodes(text)

        self.assertListEqual(what_i_want, what_i_have)


if __name__ == "__main__":
    unittest.main()
