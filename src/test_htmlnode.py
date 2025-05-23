import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_def_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("test", "BLUE", "/test/test", {"this is the day":"The Lord has made!!!"})
        node2 = HTMLNode("tester", "RED", "/test/test", {"this is the day":"The Lord has made!!!",
                                                         "alleluia":"sing to the lord!"})
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode("test", "BLUE", "/test/test", {"this is the day":"The Lord has made!!!"})
        self.assertEqual(node.props_to_html(), " this is the day The Lord has made!!!")

if __name__ == "__main__":
    unittest.main()
