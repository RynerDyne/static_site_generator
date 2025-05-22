from enum import Enum

TextType = Enum("TextType", ["NORMAL", "BOLD", "ITALIC", "CODE", "LINK", "IMAGE"])

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type =  text_type
        self.url = url

    def __eq__(self, textnode):
        if self == textnode:
            return True

    def __repr__(self):
        return f"{self}e{self.text}, {self.text_type.value}, {self.url})"


