import re
from htmlnode import *
from inline_markdown import *
from textnode import *


def markdown_to_blocks(markdown):
    split_document = markdown.split("\n\n")
    split_document = list(filter(None, split_document))
    while " " in split_document:
        split_document.remove(" ")
    for i in range(len(split_document)):
        split_document[i] = split_document[i].strip()
    return split_document


def block_to_block_type(block: str) -> str:

    type_of_block = "paragraph"

    heading = r"^#{1,6} .+$"
    code = r"^```[\s\S]+?```$"
    quote = r"^> .+$"
    unordered_list = r"^[-*] .+$"
    ordered_list = r"^\d+\. .+$"

    if re.findall(heading, block):
        type_of_block = "heading"
    if re.findall(code, block, re.MULTILINE):
        type_of_block = "code"
    if re.findall(quote, block, re.MULTILINE):
        type_of_block = "blockquote"
    if re.findall(unordered_list, block, re.MULTILINE):
        type_of_block = "unordered_list"
    if re.findall(ordered_list, block, re.MULTILINE):
        ol = block.split("\n")
        aux = 1
        list_is_ordered = True
        for element in ol:
            if not element.startswith(str(aux)):
                list_is_ordered = False
            aux += 1
        if list_is_ordered:
            type_of_block = "ordered_list"

    return type_of_block


def markdown_to_html_node(markdown: str) -> ParentNode:
    md = markdown_to_blocks(markdown)
    while "" in md:
        md.remove("")
    node_list = []
    for m in md:
        block_type = block_to_block_type(m)
        if block_type == "heading":
            count = count_hashes_at_start(m)
            node_list.append(heading_to_htmlnode(count, m))
        elif block_type == "paragraph":
            node_list.append(paragraph_to_htmlnode(m))
        elif block_type == "unordered_list":
            node_list.append(list_to_html(m, block_type))
        elif block_type == "ordered_list":
            node_list.append(list_to_html(m, block_type))
        elif block_type == "blockquote":
            node_list.append(blockquote_to_htmlnode(m))
        elif block_type == "code":
            node_list.append(code_to_htmlnode(m))
        else:
            raise ValueError("Invalid text type")
    return ParentNode("div", node_list, None)


def eliminate_empties(lista):
    md = lista.split("\n")
    while " " in md:
        md.remove(" ")
    while "" in md:
        md.remove("")
    return md


def list_to_html(lista, type):
    markdown = markdown_to_blocks(lista)
    for element in markdown:
        if type == "unordered_list":
            return unordered_list_to_html(element)
        elif type == "ordered_list":
            return ordered_list_to_html(element)


def heading_to_htmlnode(amnt: int, heading: str):
    md = heading[amnt + 1 :]
    md = text_to_textnodes(md)
    for i in range(len(md)):
        md[i] = md[i].text_node_to_html_node()
    return ParentNode(f"h{amnt}", md, None)


def code_to_htmlnode(code):
    md = code.split("\n")
    md = md[1:-1]
    md = "\n".join(md)
    code_node = []
    parent_node = []
    code_node.append(LeafNode(None, md, None))
    parent_node.append(ParentNode("code", code_node, None))
    return ParentNode("pre", parent_node, None)


def unordered_list_to_html(ul):
    md = eliminate_empties(ul)
    li_nodes = []
    for i in range(len(md)):
        md[i] = md[i].strip()
        md[i] = md[i][1:]
        md[i] = md[i].strip()
        node = text_to_textnodes(md[i])
        for i in range(len(node)):
            node[i] = node[i].text_node_to_html_node()
        li_nodes.append(ParentNode("li", node, None))
    return ParentNode("ul", li_nodes, None)


def ordered_list_to_html(ol):
    md = eliminate_empties(ol)
    li_nodes = []
    for i in range(len(md)):
        md[i] = md[i].strip()
        md[i] = md[i][2:]
        md[i] = md[i].strip()
        node = text_to_textnodes(md[i])
        for i in range(len(node)):
            node[i] = node[i].text_node_to_html_node()
        li_nodes.append(ParentNode("li", node, None))
    return ParentNode("ol", li_nodes, None)


def blockquote_to_htmlnode(blockquote: str):
    md = blockquote.split("\n")
    for i in range(len(md)):
        md[i] = md[i].strip()
        md[i] = md[i][1:]
        md[i] = md[i].strip()
    md = " ".join(md)
    md = text_to_textnodes(md)
    for i in range(len(md)):
        md[i] = md[i].text_node_to_html_node()
    return ParentNode("blockquote", md, None)


def paragraph_to_htmlnode(paragraph: str):
    md = paragraph.split("\n")
    md = " ".join(md)
    md = text_to_textnodes(md)
    for i in range(len(md)):
        md[i] = md[i].text_node_to_html_node()
    return ParentNode("p", md, None)


def count_hashes_at_start(s: str) -> int:
    count = 0
    for char in s:
        if char == "#":
            count += 1
        else:
            break
    return count
