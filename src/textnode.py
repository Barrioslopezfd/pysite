class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if(
                self.text == text_node.text and 
                self.text_type == text_node.text_type and 
                self.url == text_node.url
                ):
            return True
    def __repr__(text_node):
        return f"TextNode({text_node.text}, {text_node.text_type}, {text_node.url})"

def main():
    my_text = TextNode()
    my_text.text = 'Hola si buenas'
    my_text.text_type = 'bold'
    my_text.url = 'holasibuenas.com'

    valor = my_text.__eq__(my_text)
    
    print(valor)

    otro_valor = my_text.__repr__
