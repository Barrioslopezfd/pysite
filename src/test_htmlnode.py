import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    

    def test_props_to_html(self):
        node1 = HTMLNode('a', 'this a value', props={'href': 'google.com', 'text': '#ffffff'})
        node2 = HTMLNode('b', 'this b value', props={'href': 'facebook.com', 'text': '#000000'})
        node3 = HTMLNode('c', 'this c value', children=[node1, node2], props={'href': 'youtube.com', 'text': '#0f0f0f'})
        node1 = node1.props_to_html()
        node2 = node2.props_to_html()
        node3 = node3.props_to_html()
        
        print(node1, node2, node3, end='\n')

    def test_no_props(self):

        node = HTMLNode('b', 'this b value')
        print(node.props_to_html())
        
if __name__ == "__main__":
    unittest.main()
