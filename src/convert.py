from textnode import TextNode, TextType
from htmlnode import LeafNode

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