# Create a new function called markdown_to_blocks(markdown). It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings. 
## The .split() method can be used to split a string into blocks based on a delimiter (\n\n is a double newline).
## You should .strip() any leading or trailing whitespace from each block.
## Remove any "empty" blocks due to excessive newlines.
def markdown_to_blocks(markdown):
    markdown_inline_list = list(map(
        lambda stripped: stripped.strip(),
        filter(
        lambda list: list != '',
        markdown.split("\n\n")
    )))
    return markdown_inline_list
