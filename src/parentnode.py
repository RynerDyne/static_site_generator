from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, None, props)
        self.children = children

    def to_html(self):
        if self.tag is None:
            raise ValueError("Enter a tag argument")
        elif self.children is None:
            raise ValueError("Enter a children argument")
        else:
            html_txt = ''
            for child in self.children:
                html_txt += child.to_html()
            return f"<{self.tag}>{html_txt}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

