import unittest

from split import split_nodes_delimiter, split_nodes_images, split_nodes_links, text_to_textnodes
from textnode import TextNode, TextType

class TestSplit(unittest.TestCase):
    text_no_split = "this is a normal text"

    text_two_bold_split = "this is **first** and **second**"

    def test_nothing_to_split(self):
        candidate = TextNode(self.text_no_split, TextType.TEXT)
        result = split_nodes_delimiter([candidate], "*", TextType.BOLD)
        self.assertEqual(candidate, result[0])
        self.assertEqual(len(result), 1)

    def test_split_two_bold(self):
        candidate = TextNode(self.text_two_bold_split, TextType.TEXT)
        result = split_nodes_delimiter([candidate], "**", TextType.BOLD)

        expected_a = TextNode("this is ", TextType.TEXT)
        expected_b = TextNode("first", TextType.BOLD)
        expected_c = TextNode(" and ", TextType.TEXT)
        expected_d = TextNode("second", TextType.BOLD)

        self.assertEqual(len(result), 4)
        self.assertEqual(expected_a, result[0])
        self.assertEqual(expected_b, result[1])
        self.assertEqual(expected_c, result[2])
        self.assertEqual(expected_d, result[3])


#### IMAGES ####    
    def test_split_image_not_txt(self):
        text_images = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        candidate = TextNode(text_images, TextType.BOLD)
        result = split_nodes_images([candidate])
        self.assertEqual(candidate, result[0])
        self.assertEqual(len(result), 1)

    def test_split_image_no_image(self):
        candidate = TextNode(self.text_no_split, TextType.TEXT)
        result = split_nodes_images([candidate])
        self.assertEqual(candidate, result[0])
        self.assertEqual(len(result), 1)

    def test_split_image_only_one_image(self):
        text_images = "![to boot dev](https://www.boot.dev)"
        candidate = TextNode(text_images, TextType.TEXT)
        result = split_nodes_images([candidate])

        expected_a = TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev")
        expected = [expected_a]

        self.assertEqual(result, expected) 

    def test_split_image_only_two_images(self):
        text_images = "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        candidate = TextNode(text_images, TextType.TEXT)
        result = split_nodes_images([candidate])

        expected_a = TextNode("This is text with a link ", TextType.TEXT)
        expected_b = TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev")
        expected_c = TextNode(" and ", TextType.TEXT)
        expected_d = TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        expected = [expected_a, expected_b, expected_c, expected_d]

        self.assertEqual(result, expected)


#### LINKS ####
    def test_split_link_not_txt(self):
        text_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        candidate = TextNode(text_links, TextType.BOLD)
        result = split_nodes_links([candidate])
        self.assertEqual(candidate, result[0])
        self.assertEqual(len(result), 1)

    def test_split_link_no_link(self):
        candidate = TextNode(self.text_no_split, TextType.TEXT)
        result = split_nodes_links([candidate])
        self.assertEqual(candidate, result[0])
        self.assertEqual(len(result), 1)

    def test_split_linke_only_one_link(self):
        text_links = "[to boot dev](https://www.boot.dev)"
        candidate = TextNode(text_links, TextType.TEXT)
        result = split_nodes_links([candidate])

        expected_a = TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        expected = [expected_a]

        self.assertEqual(result, expected) 

    def test_split_link_only_two_links(self):
        text_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        candidate = TextNode(text_links, TextType.TEXT)
        result = split_nodes_links([candidate])

        expected_a = TextNode("This is text with a link ", TextType.TEXT)
        expected_b = TextNode("to boot dev", TextType.LINK, "https://www.boot.dev")
        expected_c = TextNode(" and ", TextType.TEXT)
        expected_d = TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        expected = [expected_a, expected_b, expected_c, expected_d]

        self.assertEqual(result, expected) 

####TEXT TO TEXTNODES####
    def test_text_to_textnode(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)

        expected = [
                    TextNode("This is ", TextType.TEXT),
                    TextNode("text", TextType.BOLD),
                    TextNode(" with an ", TextType.TEXT),
                    TextNode("italic", TextType.ITALIC),
                    TextNode(" word and a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" and an ", TextType.TEXT),
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                    TextNode(" and a ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://boot.dev"),
                    ]

        self.assertEqual(result, expected) 
if __name__ == "__main__":
    unittest.main()