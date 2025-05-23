import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_tag_none(self):
        node = LeafNode(None, "This is a value")
        self.assertEqual(node.to_html(), "This is a value")

    def test_value_none(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

if __name__ == '__main__':
    unittest.main()
