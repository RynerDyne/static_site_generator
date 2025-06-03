import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks

md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

#### Here is a header

> quoted
> text

1. This
2. is
3. an
4. ordered
5. list

```
Here is a block of
code
```

1. this
2. list
4. is
3. out]
5. of
6. order
"""
blocks = markdown_to_blocks(md)

# 0 p
# 1 mlp
# 2 unordered list

# 3 Header
# 4 quote
# 5 ordered list
# 6 code
# 7 out of order ordered list

class TestBlockType(unittest.TestCase):
    def test_paragraph_block(self):
        block_type = block_to_block_type(blocks[0])
        self.assertEqual(block_type,
                      BlockType.PARAGRAPH)

    def test_multiline_paragraph_block(self):
        block_type = block_to_block_type(blocks[1])
        self.assertEqual(block_type,
                      BlockType.PARAGRAPH)

    def test_heading_block(self):
        block_type = block_to_block_type(blocks[3])
        self.assertEqual(block_type,
                      BlockType.HEADING)

    def test_code_block(self):
        block_type = block_to_block_type(blocks[6])
        self.assertEqual(block_type,
                      BlockType.CODE)

    def test_quote_block(self):
        block_type = block_to_block_type(blocks[4])
        self.assertEqual(block_type,
                      BlockType.QUOTE)
 
    def test_unordered_list(self):
        block_type = block_to_block_type(blocks[2])
        self.assertEqual(block_type,
                      BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block_type = block_to_block_type(blocks[5])
        self.assertEqual(block_type,
                         BlockType.ORDERED_LIST)

    def test_ordered_list_out_of_order(self):
        block_type = block_to_block_type(blocks[7])
        self.assertEqual(block_type,
                         BlockType.PARAGRAPH)

if __name__ == '__main__':
    unittest.main()
