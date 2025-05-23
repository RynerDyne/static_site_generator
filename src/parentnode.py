from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Enter a tag argument")
        elif self.children is None:
            raise ValueError("Enter a children argument")
        else:
            html_txt = '<{tag}>'
            for child in self.children:
                html_txt = html_txt + child.to_html()
            html_txt = html_txt + '</{tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

