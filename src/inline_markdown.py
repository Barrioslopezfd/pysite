import re
from textnode import *


def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        text = node.text.split(delimeter)
        if len(text) % 2 == 0:
            raise ValueError("Delimiter not closed")
        for i in range(len(text)):
            indice = i + 1
            if text[i] == "":
                continue
            if indice % 2 == 0:
                new_nodes.append(TextNode(text[i], text_type))
            else:
                new_nodes.append(TextNode(text[i], text_type_text))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_link(nodes: list[TextNode]):

    new_nodes = []

    for node in nodes:

        text = node.text
        links = extract_markdown_links(text)

        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            l = f"[{link[0]}]({link[1]})"
            sections = text.split(l, 1)

            if len(sections) != 2:
                raise ValueError("Invalid")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes


def split_nodes_image(nodes: list[TextNode]):

    new_nodes = []

    for node in nodes:

        text = node.text
        links = extract_markdown_images(text)

        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            l = f"![{link[0]}]({link[1]})"
            sections = text.split(l, 1)

            if len(sections) != 2:
                raise ValueError("Invalid")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_image, link[1]))
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))

    return new_nodes


def text_to_textnodes(text):
    node = [TextNode(text, text_type_text)]
    node = split_nodes_delimiter(node, "**", text_type_bold)
    node = split_nodes_delimiter(node, "*", text_type_italic)
    node = split_nodes_delimiter(node, "`", text_type_code)
    node = split_nodes_link(node)
    node = split_nodes_image(node)

    return node
