from generate_pages import generate_pages_recursive
from source_to_destination import source_to_destination


def main():
    source_to_destination('./static/', './public/')
    generate_pages_recursive('./content/', './template.html', './public/')

main()
