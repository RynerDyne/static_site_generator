import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is a `text` node", TextType.TEXT)
        node2 = TextNode("This `is` a `text` node", TextType.TEXT)
        node_list = [node, node2]
        split_node = split_nodes_delimiter(node_list, '`', TextType.CODE)
        print(split_node)

    def test_img(self):
        test = TextNode(None, TextType.IMAGE, url="http://test.test")

if __name__ == "__main__":
    unittest.main()

