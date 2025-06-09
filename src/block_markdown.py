import re

from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    markdown_inline_list = list(map(
        lambda stripped: stripped.strip(),
        filter(
        lambda list: list != '',
        markdown.split("\n\n")
    )))
    return markdown_inline_list

def block_to_block_type(markdown_block):
    if re.fullmatch(r'#{1,6}.+', markdown_block):
        return BlockType.HEADING
    elif re.fullmatch(r'^`{3}.+`{3}$', markdown_block, re.MULTILINE.DOTALL):
        return BlockType.CODE
    elif re.fullmatch(r'^>.+', markdown_block, re.MULTILINE.DOTALL):
        return BlockType.QUOTE
    elif re.fullmatch(r'^- .+', markdown_block, re.MULTILINE.DOTALL):
        return BlockType.UNORDERED_LIST
    elif re.fullmatch(r'^\d+\. .+', markdown_block, re.MULTILINE.S):
        split_markdown_block = markdown_block.split('\n')
        count = 1
        for split_line in split_markdown_block:
            first = split_line[0]
            if first == str(count):
                count += 1
                if count == len(split_markdown_block):
                    return BlockType.ORDERED_LIST
            else:
                return BlockType.PARAGRAPH

    else:
        return BlockType.PARAGRAPH
