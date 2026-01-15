from textnode import TextNode, TextType

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
