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
                    new_node_list.append(split_nodes_delimiter(TextNode(split_text[i], TextType.TEXT), delimiter, text_type))
                else:
                    new_node_list.append(TextNode(split_text[i], text_type))
    return new_node_list

    # this only accepts TEXT type nodes, return other types as is
    # raise an exception if there isn't a closing delimiter
    # here is the list of inline elements per type:
    ## ** == BOLD
    ## _  == ITALICS
    ## `` == CODE

    # if the type isn't TEXT, add to list as is
    # if the type is TEXT; first split based on bold, if no bold then italics, if no italics then code; return first split node as TEXT, then the next as type, then the third should run through the function again.  if no delimiter then add node to list
