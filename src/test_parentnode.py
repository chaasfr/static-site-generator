import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    tag = "a"
    value = "awesome website"
    props = {"href":"my_url.com"}
    value_txt= "random text"
    
    child_a = LeafNode(tag=tag, value=value, props=props)
    child_b = LeafNode(value=value_txt)

    parent_a = ParentNode(tag="p",children=[child_a, child_b, child_a])
    parent_b = ParentNode(tag="tr", children = [child_b, parent_a])
    
    def test_parent_to_html(self):
        expected = """<p><a href="my_url.com">awesome website</a>random text<a href="my_url.com">awesome website</a></p>"""
        self.assertEqual(self.parent_a.to_html(), expected)

    def test_nested_parent_to_html(self):
        expected = """<tr>random text<p><a href="my_url.com">awesome website</a>random text<a href="my_url.com">awesome website</a></p></tr>"""
        self.assertEqual(self.parent_b.to_html(), expected)

if __name__ == "__main__":
    unittest.main()