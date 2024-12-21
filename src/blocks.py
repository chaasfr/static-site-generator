import re
from enum import Enum

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    block = ""
    for line in lines:
        if block == "":
            block = line
        elif line != "":
            block += "\n" + line
        else:
            blocks.append(block.strip())
            block = ""
    if len(block) > 0:
        blocks.append(block)
    return blocks


def match_heading(block):
    return re.search(r"#{1,6} .*", block) is not None

def match_code(block):
    return len(block) > 6 and block[:3] == "```" and block[-3:] == "```"

def match_quote(block):
    for line in block.split("\n"):
        if len(line) < 1 or line[0] != ">":
            return False
    return True

def match_unordered_list(block):
    for line in block.split("\n"):
        if re.search(r"[*-] .*", block) is None:
            return False
    return True

def match_ordered_list(block):
    lines = block.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        expected= f"{i+1}. "
        if len(line) < 3 or line[0:3] != expected:
            return False
    return True


class BlockType(Enum):
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED LIST"
    ORDERED_LIST = "ORDERED LIST"
    TEXT = "TEXT"

def block_to_block_type(block):   
    if match_heading(block):
        return BlockType.HEADING
    elif match_code(block):
        return BlockType.CODE
    elif match_quote(block):
        return BlockType.QUOTE
    elif match_unordered_list(block):
        return BlockType.UNORDERED_LIST
    elif match_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.TEXT
