import re
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode
from inline_markdown import text_to_text_nodes
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_to_html_node import text_node_to_html_node


def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                children_nodes.append(paragraph_block_to_html_node(block))
            case BlockType.HEADING:
                children_nodes.append(heading_block_to_html_node(block))
            case BlockType.CODE:
                children_nodes.append(code_block_to_html_node(block))
            case BlockType.QUOTE:
                children_nodes.append(quote_block_to_html_node(block))
            case BlockType.ORDERED_LIST:
                children_nodes.append(ordered_list_blocks_to_html_node(block))
            case BlockType.UNORDERED_LIST:
                children_nodes.append(unordered_list_block_to_html_node(block))
#            case _:
    return ParentNode(tag='div', children=children_nodes, props=None)

def heading_block_to_html_node(block):
    hash = re.match(r"^#{1,6}", block)
    hash_count = len(hash.group(0))
    block_value = re.findall(r"^#{1,6} (.*)", block)
    node_list = (list(map(
        lambda node: text_node_to_html_node(node),
        text_to_text_nodes(block_value[0])
    )))
    return ParentNode(f"h{str(hash_count)}", node_list)

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
    code_node = LeafNode('code', code_value)
    return ParentNode('pre', [code_node])

def quote_block_to_html_node(block):
    quote_lines = block.split("> ")
    line_text = ''
    for line in quote_lines:
        line = line.strip()
        if line == '\n' or line == '':
            continue
        line_text += f"{line}\n"
    line_text_nodes = text_to_text_nodes(line_text)
    quote_nodes = (list(map(
        lambda line: text_node_to_html_node(line),
        line_text_nodes
    )))
    return ParentNode('blockquote', quote_nodes)

def list_line_to_html_node(line):
    line_text_nodes = text_to_text_nodes(line)
    return list(map(
        lambda node: text_node_to_html_node(node),
        line_text_nodes
    ))

def ordered_list_blocks_to_html_node(block):
    order_count = 1
    ordered_list_lines = block.split('\n')
    ordered_list_nodes = []
    for i in range(0,len(ordered_list_lines)):
        line = ordered_list_lines[i].strip()
        if str(order_count) != line[0][0]:
            return paragraph_block_to_html_node(block)
        ordered_list_text = f"{line[3:]}"
        ordered_list_nodes.append(ParentNode('li', list_line_to_html_node(ordered_list_text)))
        order_count += 1
    return ParentNode('ol', ordered_list_nodes)

def unordered_list_block_to_html_node(block):
    unordered_list_lines = block.split('\n')
    unordered_list_nodes = []
    for line in unordered_list_lines:
        line = line.strip()
        if len(line) == 0:
            continue
        elif line[0] != '-':
            return paragraph_block_to_html_node(block)
        line = line.lstrip('- ')
        line_text = f"{line}"
        unordered_list_nodes.append(ParentNode('li', list_line_to_html_node(line_text)))
    return ParentNode('ul', unordered_list_nodes)

def paragraph_block_to_html_node(block):
    block_nodes = list(map(
        lambda node: text_node_to_html_node(node),
        text_to_text_nodes(block)
    ))
    return ParentNode('p', block_nodes)
