import unittest

from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestBlocks(unittest.TestCase):
##markdown to blocks
    def test_markdown_to_blocks_empty(self):
        empty = ""
        result = markdown_to_blocks(empty)
        expected = []
        self.assertEqual(expected, result)

    def test_markdown_to_blocks_std(self):
        input = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        result = markdown_to_blocks(input)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        self.assertEqual(expected,result)

### BLOCK TYPES###
    def test_block_to_block_type_text(self):
        input = "rnadom text"
        expected = BlockType.TEXT
        result = block_to_block_type(input)
        self.assertEqual(result, expected)

    def test_block_to_block_heading(self):
        input = "### TITLE"
        expected = BlockType.HEADING
        result = block_to_block_type(input)
        self.assertEqual(result, expected)

    def test_block_to_block_code(self):
        input = "```a code block ```"
        expected = BlockType.CODE
        result = block_to_block_type(input)
        self.assertEqual(result, expected)

    def test_block_to_block_quote(self):
        input = """>a quote
>on 2 lines"""
        expected = BlockType.QUOTE
        result = block_to_block_type(input)
        self.assertEqual(result, expected)

    def test_block_to_block_unordered(self):
        input = """* a list
- with 2 lines"""
        expected = BlockType.UNORDERED_LIST
        result = block_to_block_type(input)
        self.assertEqual(result, expected)

    def test_block_to_block_ordered(self):
        input = """1. a list
2. with 2 lines"""
        expected = BlockType.ORDERED_LIST
        result = block_to_block_type(input)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()