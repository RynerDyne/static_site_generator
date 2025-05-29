import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is a `text` node", TextType.TEXT)
        node_list = [node]
        split_node = split_nodes_delimiter(node_list, '`', TextType.CODE)
        self.assertEqual(split_node, [TextNode('This is a ', TextType.TEXT), TextNode('text', TextType.CODE), TextNode(' node', TextType.TEXT)])

    def test_multi_delimiter_node(self):
        node = TextNode("This is a `text` node", TextType.TEXT)
        node2 = TextNode("This `is` a `text` node", TextType.TEXT)
        node_list = [node, node2]
        split_node = split_nodes_delimiter(node_list, '`', TextType.CODE)
        self.assertEqual(split_node, [TextNode('This is a ', TextType.TEXT), TextNode('text', TextType.CODE), TextNode(' node', TextType.TEXT), TextNode('This ', TextType.TEXT), TextNode('is', TextType.CODE), TextNode(' a ', TextType.TEXT), TextNode('text', TextType.CODE), TextNode(' node', TextType.TEXT)])

if __name__ == "__main__":
    unittest.main()

