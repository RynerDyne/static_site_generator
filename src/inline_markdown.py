import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_node_list.append(node)
        elif delimiter in node.text:
            num_of_delimiter = re.findall(delimiter, node.text)
            if len(num_of_delimiter)  % 2 == 1:
                raise Exception('illegal; must have an opening and closing delimiter')
            split_text = node.text.split(delimiter)
            for i in range(0, len(split_text)):
                if i == 0:
                    new_node_list.append(TextNode(split_text[i], TextType.TEXT))
                elif i % 2 == 0:
                    new_node_list.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    new_node_list.append(TextNode(split_text[i], text_type))
        else:
            new_node_list.append(node[0])
    return new_node_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images_nodes = extract_markdown_images(node.text)
        text_remaining = node.text
        for image in images_nodes:
            image_fstring = f"![{image[0]}]({image[1]})"
            sectioned = text_remaining.split(image_fstring)
            if sectioned[0] != "":
                new_nodes.append(TextNode(sectioned[0], TextType.TEXT))
            if sectioned[1] != "" and len(sectioned[1].split(image_fstring)) != 1:
                new_nodes.append(TextNode(sectioned[1], TextType.TEXT))
            elif sectioned[1] != "":
                text_remaining = sectioned[1]
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links_nodes = extract_markdown_links(node.text)
        text_remaining = node.text
        for link in links_nodes:
            link_fstring = f"[{link[0]}]({link[1]})"
            sectioned = text_remaining.split(link_fstring)
            if sectioned[0] != "":
                new_nodes.append(TextNode(sectioned[0], TextType.TEXT))
            if sectioned[1] != "" and len(sectioned[1].split(link_fstring)) != 1:
                new_nodes.append(TextNode(sectioned[1], TextType.TEXT))
            elif sectioned[1] != "":
                text_remaining = sectioned[1]
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)



