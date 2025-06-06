from block_markdown import BlockType, block_to_block_type, markdown_to_blocks


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING and block[1] == ' ':
            return block.lstrip('# ')
    raise Exception('No \'h1\' header title in markdown')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = from_path.read()
    return 0
#  Read the markdown file at from_path and store the contents in a variable.
#  Read the template file at template_path and store the contents in a variable.
#  Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
#  Use the extract_title function to grab the title of the page.
#  Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
#  Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
