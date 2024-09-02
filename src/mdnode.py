import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        splitted_text = old_node.text.split(delimeter)
        if splitted_text[-1] == '':
            splitted_text = splitted_text[0:-1]
        if splitted_text[0] == '':
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
        delimetered_txt = ' '.join(delimetered_txt)
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


def split_nodes_image(old_nodes: list[TextNode]):
    node_list = []
    link_list = []
    aux = 0
    for nodes in old_nodes:
        old_text = nodes.text
        links = extract_markdown_images(old_text)
        for l in links:
            l = list(l)
            link_list.append(TextNode(l[0], text_type_image, l[1]))
        for l in links:
            for t in l:
                old_text = old_text.replace(f'![{t}]', f'|![text]')
                old_text = old_text.replace(f'({t})', f'(link)|')
        old_text = old_text.split("|")
        if old_text[-1]=='':
            old_text=old_text[:-1]
        node_list = list(old_text[:])
        
        for i in range(len(node_list)):
            if "![text](link)" not in node_list[i]:
                node_list[i] = TextNode(node_list[i], text_type_text)
            else:
                node_list[i] = link_list[aux]
                aux+=1

    return node_list


def split_nodes_link(old_nodes: list[TextNode]):
    node_list = []
    link_list = []
    aux = 0
    for nodes in old_nodes:
        old_text = nodes.text
        links = extract_markdown_links(old_text)
        for l in links:
            l = list(l)
            link_list.append(TextNode(l[0], text_type_link, l[1]))
        for l in links:
            for t in l:
                old_text = old_text.replace(f'[{t}]', f'|[text]')
                old_text = old_text.replace(f'({t})', f'(link)|')
        old_text = old_text.split("|")
        if old_text[-1]=='':
            old_text=old_text[:-1]
        node_list = list(old_text[:])
        
        for i in range(len(node_list)):
            if "[text](link)" not in node_list[i]:
                node_list[i] = TextNode(node_list[i], text_type_text)
            else:
                node_list[i] = link_list[aux]
                aux+=1

    return node_list
