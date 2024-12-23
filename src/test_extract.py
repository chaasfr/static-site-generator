import unittest

from extract import extract_markdown_images, extract_markdown_links, extract_title

class TestExtract(unittest.TestCase):
    def test_text_extract_nothing(self):
        input = ""
        img_result = extract_markdown_images(input)
        link_result = extract_markdown_links(input)
        self.assertEqual(len(img_result), 0)
        self.assertEqual(len(link_result), 0)

    def test_text_extract_two_images(self):
        input = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        img_result = extract_markdown_images(input)

        expected_tuple_1 = ("rick roll", "https://i.imgur.com/aKaOqIh.gif")
        expected_tuple_2 = ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        expected = [expected_tuple_1, expected_tuple_2]

        self.assertEqual(img_result, expected)

    def test_text_extract_two_links(self):
        input = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link_result = extract_markdown_links(input)

        expected_tuple_1 = ("to boot dev", "https://www.boot.dev")
        expected_tuple_2 = ("to youtube", "https://www.youtube.com/@bootdotdev")
        expected = [expected_tuple_1, expected_tuple_2]

        self.assertEqual(link_result, expected)


    def test_extract_tile(self):
        input = """"
this is not a title
# Title
got it
        """
        expected = "Title"
        
        result = extract_title(input)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()