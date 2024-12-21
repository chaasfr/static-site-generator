import re

regexp_img = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
regexp_link = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def extract_markdown_images(text):
    return re.findall(regexp_img, text)

def extract_markdown_links(text):
    return re.findall(regexp_link, text)