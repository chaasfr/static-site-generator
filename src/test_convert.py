import unittest

from convert import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode


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

if __name__ == "__main__":
    unittest.main()