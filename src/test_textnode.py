import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_1(self):
        node = TextNode("This is not a normal text node", TextType.PLAIN)
        node2 = TextNode("This should not be equal", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_2(self):
        node = TextNode("This is not a normal text node", TextType.PLAIN)
        node2 = TextNode("This should not be equal", TextType.PLAIN)
        self.assertNotEqual(node, node2)
    def test_3(self):
        node = TextNode("This is not a normal text node", TextType.PLAIN)
        node2 = TextNode("This is not a normal text node", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_4(self):
        node = TextNode("This is not a normal text node", TextType.PLAIN,"www.google.com")
        node2 = TextNode("This is not a normal text node", TextType.PLAIN,"www.google.com")
        self.assertEqual(node, node2)
    def test_5(self):
        node = TextNode("This is not a normal text node", TextType.PLAIN,"www.google.com")
        node2 = TextNode("This is not a normal text node", TextType.PLAIN,"www.amazon.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
