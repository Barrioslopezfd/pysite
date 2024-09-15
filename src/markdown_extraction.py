import os
import re
from pathlib import Path
from block_markdown import markdown_to_html_node


def extract_title(markdown):
    heading = re.findall(r"^# .+$", markdown, re.MULTILINE)
    if heading == "":
        raise Exception("No header")
    heading = "".join(heading)
    heading = heading[1:]
    heading = heading.strip()

    return heading


def generate_page_recursively(fr):
    dst_tree = os.listdir(fr)
    if dst_tree == []:
        return
    for d in dst_tree:
        temp = os.path.join(fr, d)
        if os.path.isfile(temp):
            aux = temp.replace(".md", ".html")
            aux = aux.replace("content", "public")
            generate_page(temp, "template.html", aux)
        else:
            generate_page_recursively(temp)


def generate_page(from_path, template_path, to_path):
    print(f"Generating page from {from_path} to {to_path} using {template_path}")
    md = read_file(from_path)
    template = read_file(template_path)
    title = extract_title(md)
    html_string = markdown_to_html_node(md)
    html_string = html_string.to_html()
    template = template.replace(" {{ Title }} ", title)
    template = template.replace("{{ Content }}", html_string)

    temp = to_path.split("/")
    temp = temp[:-1]
    temp = "/".join(temp)
    if not os.path.exists(temp):
        os.makedirs(temp)
    f = open(to_path, "w")
    f.write(template)
    f.close()


def read_file(path):
    with open(path) as f:
        return f.read()
