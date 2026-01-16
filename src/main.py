from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode, HTMLNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag='b', value=text_node.text)
    
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag='i', value=text_node.text)
    
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag='code', value=text_node.text)
    
    elif text_node.text_type == TextType.LINK:
        if not text_node.href:
            raise Exception(f"href attribute is required for {TextType.LINK.name}")
        return LeafNode(tag='a', value=text_node.text, props={"href": text_node.href})
    
    elif text_node.text_type == TextType.IMAGE:
        if not (text_node.src and text_node.alt):
            raise Exception(f"src and alt attributes are required for {TextType.IMAGE.name}")
        return LeafNode(tag='img', value="", props={"src": text_node.src, "alt": text_node.alt})
    
    else:
        raise Exception(f"Unsupported TextType: {text_node.text_type}")

def main():
    # Create a new TextNode object with some dummy values
    node = TextNode(
        text="Sample Text",
        text_type=TextType.LINK,
        url="https://example.com"
    )
    
    # Print the TextNode object to see its string representation
    print(node)

if __name__ == "__main__":
    main()
