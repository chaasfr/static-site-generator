import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, markdown_to_html_node


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

### markdown to html
    def test_markdown_to_html_empty(self):
        input=""
        result = markdown_to_html_node(input)
        
        expected= ParentNode(tag="div",children=[])
        
        self.assertEqual(expected,result)

    def test_markdown_to_html_paragraph(self):
        input="paragraph"
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(tag="p",value= "paragraph")
        expected = ParentNode(tag="div",children=[leafnode])
        
        self.assertEqual(expected,result)

    def test_markdown_to_html_code(self):
        input="""```code de ouf
lol```"""
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(tag="code",value= """code de ouf
lol""")
        parentNode = ParentNode(tag="pre", children=[leafnode])
        expected = ParentNode(tag="div",children=[parentNode])
        
        self.assertEqual(expected,result)
        

    def test_markdown_to_html_quote(self):
        input=""">une belle quote
>de boeuf lol"""
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(tag="blockquote",value= """une belle quote
de boeuf lol""")
        expected = ParentNode(tag="div",children=[leafnode])

        self.assertEqual(expected,result)

    def test_markdown_to_html_heading(self):
        input="### TITLE"
        result = markdown_to_html_node(input)
        
        leafnode = LeafNode(tag="h3",value= "TITLE")
        expected = ParentNode(tag="div",children=[leafnode])

        self.assertEqual(expected,result)

    def test_markdown_to_html_unordered_list(self):
        input="""- item
- item2"""
        result = markdown_to_html_node(input)
        
        leafnode1 = LeafNode(tag="li",value="item")
        leafnode2 = LeafNode(tag="li", value="item2")
        parent = ParentNode(tag="ul",children=[leafnode1, leafnode2])
        expected = ParentNode(tag="div",children=[parent])

        self.assertEqual(expected,result)

    def test_markdown_to_html_ordered_list(self):
        input="""1. learn
2. use"""
        result = markdown_to_html_node(input)
        
        leafnode1 = LeafNode(tag="li",value="learn")
        leafnode2 = LeafNode(tag="li", value="use")
        parent = ParentNode(tag="ol",children=[leafnode1, leafnode2])
        expected = ParentNode(tag="div",children=[parent])

        self.assertEqual(expected,result)

if __name__ == "__main__":
    unittest.main()