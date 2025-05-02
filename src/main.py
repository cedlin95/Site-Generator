from textnode import *
from htmlnode import *

def main():
    node = TextNode("Hello world", TextType.BOLD)
    print(node.__repr__())

    props = None
    
    htmltest = HTMLNODE("test","test","test",props)
    print(htmltest.props_to_html())

main()