from blocks import markdown_to_blocks, block_to_block_type, BlockType

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
        return "".join(map(lambda x: f" {x[0]}=\"{x[1]}\"", self.props.items()))

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


def text_block_to_html_node(block):
    return LeafNode(tag="p", value=block)

def heading_block_to_html_node(block):
    i=0
    curr_char= "#"
    value = block
    while curr_char == "#":
        value = value[1:]
        curr_char = value[0]
        i += 1
    return LeafNode(tag=f"h{i}", value=value.lstrip())

def code_block_to_html_node(block):
    leafnode = LeafNode(tag="code", value=block[3:-3])
    return ParentNode(tag="pre", children=[leafnode])

def quote_block_to_html_node(block):
    lines =[]
    for line in block.split("\n"):
        lines.append(line[1:])
    return LeafNode(tag="blockquote",value="\n".join(lines))

def unordered_list_block_to_html_node(block):
    children = []
    for line in block.split("\n"):
        node = LeafNode(tag="li",value=line[2:])
        children.append(node)
    return ParentNode(tag="ul",children=children)

def ordered_list_block_to_html_node(block):
    children = []
    for line in block.split("\n"):
        node = LeafNode(tag="li",value=line[3:])
        children.append(node)
    return ParentNode(tag="ol",children=children)

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.TEXT:
            return text_block_to_html_node(block)
        case BlockType.HEADING:
            return heading_block_to_html_node(block)
        case BlockType.CODE:
            return code_block_to_html_node(block)
        case BlockType.QUOTE:
            return quote_block_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_block_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_block_to_html_node(block)
        case _:
            raise NotImplementedError

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        nodes.append(block_to_html_node(block, block_type))
    return ParentNode(tag="div",children=nodes)
