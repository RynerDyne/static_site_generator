import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        test = TextNode(None, TextType.IMAGE, url="http://test.test")
        tester = text_node_to_html_node(test)
        self.assertEqual(tester.tag, 'img')
        self.assertEqual(tester.value, "")
        self.assertEqual(tester.props, {"http://test.test": 'alt'})

if __name__ == "__main__":
    unittest.main()
