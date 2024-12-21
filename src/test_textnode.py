import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.text_type, TextType.ITALIC)

    def test_url(self):
        url = "my_url.com"
        node = TextNode("This is a text node", TextType.BOLD, url)
        self.assertEqual(node.url, url)

    def test_text(self):
        text = "random test text"
        node = TextNode(text, TextType.BOLD, None)
        self.assertEqual(node.text, text)

if __name__ == "__main__":
    unittest.main()