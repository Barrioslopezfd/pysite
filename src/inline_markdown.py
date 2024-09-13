import re
from textnode import *


def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        splitted_text = old_node.text.split(delimeter)
        if len(splitted_text) == 0:
            continue
        if splitted_text[-1] == "":
            splitted_text = splitted_text[0:-1]
        if splitted_text[0] == "":
            splitted_text = splitted_text[1:]
        old_node_txt_splitted = old_node.text.split()
        delimetered_txt = []
        inside_delimited = False
        for word in old_node_txt_splitted:
            if delimeter in word and not inside_delimited:
                delimetered_txt.append(word)
                if delimeter in word[-3:]:
                    continue
                inside_delimited = True
                continue
            elif inside_delimited:
                if delimeter in word:
                    inside_delimited = False
                    delimetered_txt.append(word)
                    continue
                delimetered_txt.append(word)
        delimetered_txt = " ".join(delimetered_txt)
        for text in splitted_text:
            if text in delimetered_txt:
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, text_type_text))
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
