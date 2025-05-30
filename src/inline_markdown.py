import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node_list.append(node)
            continue
        split = []
        split_text = node.text.split(delimiter)
        if len(split_text)  % 2 == 0:
            raise ValueError('illegal; must have an opening and closing delimiter')
        for i in range(0, len(split_text)):
            if split_text[i] == '':
                continue
            elif i % 2 == 0:
                split.append(TextNode(split_text[i], TextType.TEXT))
            else:
                split.append(TextNode(split_text[i], text_type))
        new_node_list.extend(split)
    return new_node_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_remaining = node.text
        images_nodes = extract_markdown_images(text_remaining)
        if len(images_nodes) == 0:
            new_nodes.append(node)
            continue
        for image in images_nodes:
            image_fstring = f"![{image[0]}]({image[1]})"
            sectioned = text_remaining.split(image_fstring)
            if len(sectioned) != 2:
                raise ValueError('illegal; image section not closed')
            if sectioned[0] != "":
                new_nodes.append(TextNode(sectioned[0], TextType.TEXT))
            text_remaining = sectioned[1]
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if text_remaining != '':
            new_nodes.append(TextNode(text_remaining, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text_remaining = node.text
        links_nodes = extract_markdown_links(text_remaining)
        if len(links_nodes) == 0:
            new_nodes.append(node)
            continue
        for link in links_nodes:
            link_fstring = f"[{link[0]}]({link[1]})"
            sectioned = text_remaining.split(link_fstring)
            if len(sectioned) != 2:
                raise ValueError('illegal; link section not closed')
            if sectioned[0] != "":
                new_nodes.append(TextNode(sectioned[0], TextType.TEXT))
            text_remaining = sectioned[1]
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        if text_remaining != '':
            new_nodes.append(TextNode(text_remaining, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[([^\]]*)\]\(([^\]]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\]]*)\]\(([^\]]*)\)", text)

def text_to_text_nodes(text):
    text_to_node = [TextNode(text, TextType.TEXT)]
    to_bold = split_nodes_delimiter(text_to_node, "**", TextType.BOLD)
    to_italics = split_nodes_delimiter(to_bold, '_', TextType.ITALICS)
    to_code = split_nodes_delimiter(to_italics, '`', TextType.CODE)
    to_link = split_nodes_link(to_code)
    to_image = split_nodes_image(to_link)
    return to_image
