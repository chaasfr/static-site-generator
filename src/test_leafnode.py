import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    tag = "a"
    value = "awesome website"
    value_txt = "random text"
    props = {"href":"my_url.com"}
    
    node_a = LeafNode(tag=tag, value=value, props=props)
    node_b = LeafNode(value=value_txt)
    
    def test_props_to_html(self):
        expected = "<a href=\"my_url.com\">awesome website</a>"
        self.assertEqual(self.node_a.to_html(), expected)

    def test_constr(self):
        self.assertEqual(self.node_a.tag, self.tag)
        self.assertEqual(self.node_a.value, self.value)
        self.assertEqual(self.node_a.children, None)

    def test_constr(self):
        self.assertEqual(self.node_b.tag, None)
        self.assertEqual(self.node_b.value, self.value_txt)
        self.assertEqual(self.node_b.children, None)

if __name__ == "__main__":
    unittest.main()