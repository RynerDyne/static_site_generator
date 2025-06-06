class HTMLNode():
    # props is to be a dictionar of key:value pairs
    ## ex. {"href": "https://boot.dev"}
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is not None:
            return "".join(list(map(
                lambda attribute: f" {attribute} {self.props[attribute]}",
                self.props
            )))

    def __eq__(self, other):
        if (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
