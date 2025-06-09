from generate_pages import generate_page
from source_to_destination import source_to_destination


def main():
    source_to_destination('./static/', './public/')
    generate_page('./content/index.md', './template.html', './public/')

main()
