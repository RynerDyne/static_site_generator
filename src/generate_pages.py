import os
from os.path import isfile
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from markdown_to_html_node import markdown_to_html_node


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING and block[1] == ' ':
            return block.lstrip('# ')
    raise Exception('No \'h1\' header title in markdown')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    md_to_html_nodes = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    html = md_to_html_nodes.to_html()

    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    with open(os.path.join(dest_path, 'index.html'), 'w') as f:
        f.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    list_of_content_dir = os.listdir(dir_path_content)
    for list in list_of_content_dir:
        list_path = os.path.join(dir_path_content, list)
        if os.path.isfile(list_path):
            generate_page(list_path, template_path, dest_dir_path)
        else:
            list_dest = os.path.join(dest_dir_path, list)
            os.mkdir(list_dest)
            generate_pages_recursive(list_path, template_path, list_dest)
