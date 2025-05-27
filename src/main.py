from textnode import TextNode, TextType
from leafnode import LeafNode
import textnode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
           return LeafNode(None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALICS:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, props={'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', props={text_node.url: 'alt'})
        case _:
            raise Exception('text_type of TextNode must be of approved type!')


def main():
    name = TextNode("created test text", TextType.LINK, "http://boot.dev")
    print(name)

main()
