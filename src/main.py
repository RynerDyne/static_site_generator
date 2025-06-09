import sys

from generate_pages import generate_pages_recursive
from source_to_destination import source_to_destination


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    source_to_destination('./static/', './docs/')
    generate_pages_recursive('./content/', './template.html', './docs/', basepath)

main()
