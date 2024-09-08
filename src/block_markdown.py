import re


def markdown_to_blocks(markdown):
    split_document = markdown.split("\n\n")

    split_document = list(filter(None, split_document))

    for i in range(len(split_document)):
        split_document[i] = split_document[i].strip()

    return split_document


def block_to_block_type(block: str) -> str:

    type_of_block = "paragraph"

    heading = r"^#{1,6} .+$"
    code = r"^```[\s\S]+?```$"
    quote = r"^> .+$"
    unordered_list = r"^[-*] .+$"
    ordered_list = r"^\d .$"

    print(block)

    if re.findall(heading, block):
        type_of_block = "heading"
    if re.findall(code, block):
        type_of_block = "code"

    if re.findall(quote, block):
        type_of_block = "quote"
    if re.findall(unordered_list, block, re.MULTILINE):
        type_of_block = "unordered_list"
    if re.findall(ordered_list, block):
        ol = block.split("\n")
        aux = 1
        list_is_ordered = False
        for element in ol:
            if element[0] == aux:
                if aux == len(ol):
                    list_is_ordered = True
                aux += 1
        if list_is_ordered:
            type_of_block = "ordered_list"

    return type_of_block
