from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, None, None, props)
        self.value = value

    def to_html(self):
        if self.value is None:
            raise ValueError("Enter a value argument")
        elif self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
