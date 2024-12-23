import re

regexp_img = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
regexp_link = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"


def extract_markdown_images(text):
    return re.findall(regexp_img, text)

def extract_markdown_links(text):
    return re.findall(regexp_link, text)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if len(line) > 1 and line[0] == "#" and line[1] != "#":
            return line[1:].lstrip()
    raise Exception("No h1 title found")