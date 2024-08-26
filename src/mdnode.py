from textnode import *

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
        splitted_text = old_node.text.split(delimeter)
        if splitted_text[-1] == '':
            splitted_text = splitted_text[0:-1]
        old_node_txt_splitted = old_node.text.split()
        delimetered_txt = []
        inside = False
        for i in range(len(old_node_txt_splitted)):
            if delimeter in old_node_txt_splitted[i] or inside == True:
                inside = True
                delimetered_txt.append(old_node_txt_splitted[i])
                if delimeter in old_node_txt_splitted[i]:
                    inside = False
        delimetered_txt = ' '.join(delimetered_txt)
        for text in splitted_text:
            if text in delimetered_txt:
                new_nodes.append(TextNode(text, text_type))
            else:
                new_nodes.append(TextNode(text, text_type_text))
    return new_nodes


