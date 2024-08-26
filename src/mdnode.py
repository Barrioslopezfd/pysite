from re import split
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


