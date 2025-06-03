# Split the markdown into blocks (you already have a function for this)
# Loop over each block:
# 
#     Determine the type of block (you already have a function for this)
#     Based on the type of block, create a new HTMLNode with the proper data
#     Assign the proper child HTMLNode objects to the block node. I created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions (think TextNode -> HTMLNode).
#     The "code" block is a bit of a special case: it should not do any inline markdown parsing of its children. I didn't use my text_to_children function for this block type, I manually made a TextNode and used text_node_to_html_node.
# 
# Make all the block nodes children under a single parent HTML node (which should just be a div) and return it.

import re
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode
from inline_markdown import text_to_text_nodes
from text_node_to_html_node import text_node_to_html_node


# for later # def markdown_to_html_node(markdown):
# for later #     md_blocks = markdown_to_blocks(markdown)
# for later #     children_nodes = []
# for later #     for block in md_blocks:
# for later #         block_type = block_to_block_type(block)
# for later #     return HTMLNode(tag='div', value=None, children=children_nodes, props=None)

def heading_block_to_html_node(block):
    hash = re.match(r"^#{1,6}", block)
    hash_count = len(hash.group(0))
    block_value = re.findall(r"^#{1,6} (.*)", block)
    node_list = (list(map(
        lambda node: text_node_to_html_node(node),
        text_to_text_nodes(block_value[0])
    )))
    return HTMLNode(f"h{str(hash_count)}", None, node_list)

def code_block_to_html_node(block):
    block_lines = block.split("\n")
    code_value = ''
    for line in block_lines:
        line = line.strip()
        if line == '':
            continue
        elif line == "```":
            continue
        else:
            code_value += f"{line}\n"
    code_node = HTMLNode('code', code_value)
    return HTMLNode('pre', None, [code_node])

def quote_block_to_html_node(block):
    quote_lines = block.split("> ")
    
    print(quote_lines)
# re.fullmatch(r'^>.+', markdown_block, re.MULTILINE.DOTALL)
