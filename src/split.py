from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            text_split = node.text.split(delimiter)
            if len(text_split) % 2 == 0:
                raise Exception(f"invalid Markdown syntax - delimiter {delimiter} not closed in {node.text}")
            for i in range(len(text_split)):
                if len(text_split[i]) > 0:
                    new_text_type = node.text_type if i % 2 == 0 else text_type
                    new_node = TextNode(text_split[i], new_text_type)
                    result.append(new_node)
    return result

#transforms AAAABAAAAACAAAAADAAA
#into AAAAA, B, AAAAA, C, AAAA, D, AAAAA
#where B, C, D are images nodes
def spliter_img(imgs,txt):
    result = []
    if len(imgs) == 0:
        if len(txt) > 0:
            result.append(TextNode(txt, TextType.TEXT))
    else:
        img = imgs[0]
        sections = txt.split(f"![{img[0]}]({img[1]})", 1)
        init_txt = sections[0]
        new_text_node_img = TextNode(img[0], TextType.IMAGE, img[1])
        if len(init_txt) > 0:
            new_text_node_text = TextNode(init_txt, TextType.TEXT)
            result.append(new_text_node_text)
        result.append(new_text_node_img)
        result += spliter_img(imgs[1:], sections[1])
    return result


def split_nodes_images(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(images) == 0 and len(node.text) > 0:
                result.append(node)
            else:
                result += spliter_img(images, node.text)
    return result

            
#transforms AAAABAAAAACAAAAADAAA
#into AAAAA, B, AAAAA, C, AAAA, D, AAAAA
#where B, C, D are links nodes
def spliter_link(links,txt):
    result = []
    if len(links) == 0:
        if len(txt) > 0:
            result.append(TextNode(txt, TextType.TEXT))
    else:
        link = links[0]
        sections = txt.split(f"[{link[0]}]({link[1]})", 1)
        init_txt = sections[0]
        new_text_node_link = TextNode(link[0], TextType.LINK, link[1])
        if len(init_txt) > 0:
            new_text_node_text = TextNode(init_txt, TextType.TEXT)
            result.append(new_text_node_text)
        result.append(new_text_node_link)
        result += spliter_link(links[1:], sections[1])
    return result


def split_nodes_links(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(links) == 0 and len(node.text) > 0:
                result.append(node)
            else:
                result += spliter_link(links, node.text)
    return result


def split_nodes_bold(nodes):
    return split_nodes_delimiter(nodes, "**", TextType.BOLD)

def split_nodes_italic(nodes):
    return split_nodes_delimiter(nodes, "*", TextType.ITALIC)

def split_nodes_code(nodes):
    return split_nodes_delimiter(nodes, "`", TextType.CODE)

def splitter(nodes):
    funcs = [split_nodes_bold, split_nodes_italic, split_nodes_code, split_nodes_links, split_nodes_images]
    local_nodes = nodes.copy()
    for func in funcs:
        local_nodes = func(local_nodes)
    return local_nodes

def text_to_textnodes(text):
    initial_nodes = [TextNode(text, TextType.TEXT)]
    return splitter(initial_nodes)