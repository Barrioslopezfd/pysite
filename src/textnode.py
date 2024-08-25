from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
                self.text == other.text and 
                self.text_type == other.text_type and 
                self.url == other.url
        ) 
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def text_node_to_html_node(self):
        if self.text_type == text_type_text:
            node = LeafNode(None, self.text, None)
        elif self.text_type == text_type_bold:
            node = LeafNode('b', self.text, None)           
        elif self.text_type == text_type_italic:
            node = LeafNode('i', self.text, None)
        elif self.text_type == text_type_code:
            node = LeafNode('code', self.text, None)
        elif self.text_type == text_type_link:
            node = LeafNode('a', self.text, {'href': self.url })
        elif self.text_type == text_type_image:
            node = LeafNode('img', '', { 'src': self.url, 'alt': self.text })
        else: 
            raise Exception("Invalid text type")
        return node.to_html()





