from blocks import BlockType, block_to_block_type, markdown_to_blocks
from split import text_to_textnodes
from textnode import TextType
from htmlnode import LeafNode, ParentNode

def text_node_to_html_node(text_node):
    tag = None
    value = None
    props = None
    match text_node.text_type:

        case TextType.TEXT:
            value = text_node.text

        case TextType.BOLD:
            tag = "b"
            value = text_node.text

        case TextType.ITALIC:
            tag = "i"
            value = text_node.text

        case TextType.CODE:
            tag = "code"
            value = text_node.text

        case TextType.LINK:
            tag = "a"
            value = text_node.text
            props = {"href": text_node.url}
        
        case TextType.IMAGE:
            tag = "img"
            value = ""
            props = {
                "src": text_node.url,
                "alt": text_node.text
            }

        case _:
            raise Exception(f"text type {text_node.text_type} not supported")

    return LeafNode(tag=tag, value=value, props=props)



def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return list(map(text_node_to_html_node, textnodes))

def text_block_to_html_node(block):
    children = text_to_children(block)
    return ParentNode(tag="p", children=children)

def heading_block_to_html_node(block):
    i=0
    curr_char= "#"
    value = block
    while curr_char == "#":
        value = value[1:]
        curr_char = value[0]
        i += 1
    text = value.lstrip()
    children = text_to_children(text)
    return ParentNode(tag=f"h{i}", children=children)

def code_block_to_html_node(block):
    children = text_to_children(block[3:-3])
    ParentCodeNode = ParentNode(tag="code", children=children)
    return ParentNode(tag="pre", children=[ParentCodeNode])

def quote_block_to_html_node(block):
    lines =[]
    for line in block.split("\n"):
        lines.append(line[1:].lstrip())
    text = "\n".join(lines)
    children = text_to_children(text)
    return ParentNode(tag="blockquote",children=children)

def unordered_list_block_to_html_node(block):
    children = []
    for line in block.split("\n"):
        text = line[2:]
        child_children= text_to_children(text)
        child = ParentNode(tag="li",children=child_children)
        children.append(child)
    return ParentNode(tag="ul",children=children)

def ordered_list_block_to_html_node(block):
    children = []
    for line in block.split("\n"):
        text = line[3:]
        child_children = text_to_children(text)
        child = ParentNode(tag="li",children=child_children)
        children.append(child)
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
