class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"""HTMLNode:
        tag = {self.tag}
        value = {self.value}
        children = {self.children}
        props = {self.props}
        """

    def __eq__(self, htmlnode):
        return (self.tag == htmlnode.tag
            and self.value == htmlnode.value
            and self.props == htmlnode.props
            and self.children == htmlnode.children)


    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props:
            return "".join(map(lambda x: f" {x[0]}=\"{x[1]}\"", self.props.items()))
        else:
            return ""

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value.")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent node must have a tag.")
        elif self.children is None:
            raise ValueError("parent node must have children.")
        else:
            children_html = "".join(map(lambda x: x.to_html(), self.children))
            return f"<{self.tag}>{children_html}</{self.tag}>"
        