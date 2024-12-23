import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    tag = "h1"
    value = "my_title"
    props = {"href":"my_url.com", "target" : "not_blank"}
    
    node_a = HTMLNode(tag=tag, value=value, props=props)
    
    def test_props_to_html(self):
        expected = " href=\"my_url.com\" target=\"not_blank\""
        self.assertEqual(self.node_a.props_to_html(), expected)

    def test_constr(self):
        self.assertEqual(self.node_a.tag, self.tag)
        self.assertEqual(self.node_a.value, self.value)
        self.assertEqual(self.node_a.children, None)

if __name__ == "__main__":
    unittest.main()