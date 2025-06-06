import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from markdown_to_html_node import code_block_to_html_node, heading_block_to_html_node, ordered_list_blocks_to_html_node, paragraph_block_to_html_node, quote_block_to_html_node, unordered_list_block_to_html_node
from parentnode import ParentNode


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
                         ParentNode('pre', [
                         LeafNode('code', "This is a code\nblock **bold**\n")
                         ]))

    def test_quote_block_to_html_node(self):
        quote_md_block = """
        > This
        > _is a_
        > quote **block**
        """
        expected_result_node_list = [
            LeafNode(None, "This\n"),
            LeafNode("i", "is a"),
            LeafNode(None, "\nquote "),
            LeafNode("b", "block"),
            LeafNode(None, "\n")
        ]
        self.assertEqual(quote_block_to_html_node(quote_md_block),
                         HTMLNode('blockquote', None, expected_result_node_list))

    def test_ordered_list_blocks_to_html_node(self):
        ordered_list_md_block = """
        1. Here
        2. is **an** ordered
        3. [list](list.test.test)
        """
        self.assertEqual(ordered_list_blocks_to_html_node(ordered_list_md_block),
                         HTMLNode('ol', None, [
                         HTMLNode('li', None, [LeafNode(None, "Here\n")]),
                         HTMLNode('li', None, [LeafNode(None, 'is '),
                                               LeafNode('b', 'an'),
                                               LeafNode(None, ' ordered\n')]),
                         HTMLNode('li', None, [LeafNode('a', 'list', {'href': 'list.test.test'}),
                                               LeafNode(None, '\n')])
                         ]))

    def test_wrong_ordered_list_blocks_to_html_node(self):
        ordered_list_md_block = """
        1. Here
        4. is **an** ordered
        3. [list](list.test.test)
        """
        self.assertEqual(ordered_list_blocks_to_html_node(ordered_list_md_block),
                         HTMLNode('p', None, [
                         LeafNode(None, '\n        1. Here\n        4. is '),
                         LeafNode('b', 'an'),
                         LeafNode(None, ' ordered\n        3. '),
                         LeafNode('a', 'list', {'href': 'list.test.test'}),
                         LeafNode(None, '\n        ')
                         ]))

    def test_unordered_list_blocks_to_html_node(self):
        unordered_list_md_block = """
        - Here
        - is **an** unordered
        - ![image](image.test.test)
        """
        self.assertEqual(unordered_list_block_to_html_node(unordered_list_md_block),
                         HTMLNode('ul', None, [
                         HTMLNode('li', None, [LeafNode(None, "Here\n")]),
                         HTMLNode('li', None, [LeafNode(None, 'is '),
                                               LeafNode('b', 'an'),
                                               LeafNode(None, ' unordered\n')]),
                         HTMLNode('li', None, [LeafNode('img', '', {'image.test.test':'alt'}),
                                               LeafNode(None, '\n')])
                         ]))

    def test_wrong_unordered_list_blocks_to_html_node(self):
        unordered_list_md_block = """
        - Here
          is **an** unordered
        - ![image](image.test.test)
        """
        self.assertEqual(unordered_list_block_to_html_node(unordered_list_md_block),
                         HTMLNode('p', None, [
                         LeafNode(None, '\n        - Here\n          is '),
                         LeafNode('b', 'an'),
                         LeafNode(None, ' unordered\n        - '),
                         LeafNode('img', '', {'image.test.test':'alt'}),
                         LeafNode(None, '\n        ')
                         ]))

    def test_paragraph_blocks_to_html_node(self):
        paragraph_md_block = """
        This here is a **paragraph**!
        """
        self.assertEqual(paragraph_block_to_html_node(paragraph_md_block),
                         HTMLNode('p', None, [
                         LeafNode(None, "\n        This here is a "),
                         LeafNode('b', 'paragraph'),
                         LeafNode(None, '!\n        ')
                         ]))
