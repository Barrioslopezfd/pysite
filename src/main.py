from file_management import copy_from_to
from markdown_extraction import generate_page_recursively


def main():

    copy_from_to("static", "public")
    generate_page_recursively("content")


main()
