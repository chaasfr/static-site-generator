import unittest

from convert import markdown_to_html_node, text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode


class TestConvert(unittest.TestCase):
    def test_text_to_html_text(self):
        txt_node = TextNode("This is a text node", TextType.TEXT)
        expected = LeafNode(value="This is a text node")
        result = text_node_to_html_node(txt_node)
        self.assertEqual(result, expected)

    def test_text_to_html_bold(self):
        txt_node = TextNode("This is bold", TextType.BOLD)
        expected = LeafNode(value="This is bold", tag="b")
        result = text_node_to_html_node(txt_node)
        self.assertEqual(result, expected)

    def test_text_to_html_italic(self):
        txt_node = TextNode("This is italic", TextType.ITALIC)
        expected = LeafNode(value="This is italic", tag="i")
        result = text_node_to_html_node(txt_node)
        self.assertEqual(result, expected)

    def test_text_to_html_code(self):
        txt_node = TextNode("This is code", TextType.CODE)
        expected = LeafNode(value="This is code", tag="code")
        result = text_node_to_html_node(txt_node)
        self.assertEqual(result, expected)

    def test_text_to_html_link(self):
        txt_node = TextNode("This is link", TextType.LINK, "myurl.com")
        expected = LeafNode(value="This is link", tag="a", props={"href":"myurl.com"})
        result = text_node_to_html_node(txt_node)
        self.assertEqual(result, expected)

    def test_text_to_html_image(self):
        txt_node = TextNode("This is descr", TextType.IMAGE, "myimg.com")
        expected = LeafNode(value="", tag="img", props= {"src":"myimg.com", "alt": "This is descr"})
        result = text_node_to_html_node(txt_node)
        self.assertEqual(result, expected)


### markdown to html
    def test_markdown_to_html_empty(self):
        input=""
        result = markdown_to_html_node(input)
        
        expected= ParentNode(tag="div",children=[])
        
        self.assertEqual(expected,result)

    def test_markdown_to_html_paragraph(self):
        input="paragraph"
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(value= "paragraph")
        parentNode = ParentNode(tag="p",children=[leafnode])
        expected = ParentNode(tag="div",children=[parentNode])
        
        self.assertEqual(expected,result)

    def test_markdown_to_html_code(self):
        input="""```code de ouf
lol```"""
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(value= """code de ouf
lol""")
        parentcodeNode = ParentNode(tag="code", children=[leafnode])
        parentNode = ParentNode(tag="pre", children=[parentcodeNode])
        expected = ParentNode(tag="div",children=[parentNode])

        self.assertEqual(expected,result)
        
        
    def test_markdown_to_html_quote(self):
        input=""">une belle quote
>de boeuf lol"""
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(value= """une belle quote
de boeuf lol""")
        parentNode = ParentNode(tag="blockquote", children=[leafnode])
        expected = ParentNode(tag="div",children=[parentNode])

        self.assertEqual(expected,result)

    def test_markdown_to_html_heading(self):
        input="### TITLE"
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(value= "TITLE")
        parentTitleNode = ParentNode(tag="h3", children=[leafnode])
        expected = ParentNode(tag="div",children=[parentTitleNode])

        self.assertEqual(expected,result)


    def test_markdown_to_html_unordered_list(self):
        input="""- item
- item2"""
        result = markdown_to_html_node(input)
        
        leafnode1 = LeafNode(value="item")
        parentNode1 = ParentNode(tag="li", children=[leafnode1])
        leafnode2 = LeafNode(value="item2")
        parentNode2 = ParentNode(tag="li", children=[leafnode2])
        parent = ParentNode(tag="ul",children=[parentNode1, parentNode2])
        expected = ParentNode(tag="div",children=[parent])


        self.assertEqual(expected,result)

    def test_markdown_to_html_ordered_list(self):
        input="""1. learn
2. use"""
        result = markdown_to_html_node(input)
        
        leafnode1 = LeafNode(value="learn")
        parentNode1 = ParentNode(tag="li", children=[leafnode1])
        leafnode2 = LeafNode(value="use")
        parentNode2 = ParentNode(tag="li", children=[leafnode2])
        parent = ParentNode(tag="ol",children=[parentNode1, parentNode2])
        expected = ParentNode(tag="div",children=[parent])

        self.assertEqual(expected,result)
        
if __name__ == "__main__":
    unittest.main()