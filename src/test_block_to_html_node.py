import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_to_html_node import code_block_to_html_node, heading_block_to_html_node, quote_block_to_html_node


class TestBlockToHTML(unittest.TestCase):
    def test_heading_block_to_html_node(self):
        heading_md_block = "#### this is a test ## and this **as** well"
        expected_result_node_list = [
            LeafNode(None, "this is a test ## and this "),
            LeafNode('b', "as"),
            LeafNode(None, " well")
        ]
        self.assertEqual(heading_block_to_html_node(heading_md_block),
                         HTMLNode('h4', None, expected_result_node_list))

    def test_code_block_to_html_node(self):
        code_md_block = """
        ```
        This is a code\nblock **bold**
        ```
        """
        self.assertEqual(code_block_to_html_node(code_md_block),
                         HTMLNode('pre', None, [
                         HTMLNode('code', "This is a code\nblock **bold**\n")
                         ]))

    def test_quote_block_to_html_node(self):
        quote_md_block = """
        > This
        > __is a__
        > quote **block**
        """
        quote_block_to_html_node(quote_md_block)
