from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = 1
    BOLD_TEXT = 2
    ITALIC_TEXT = 3
    CODE_TEXT = 4
    LINK = 5
    IMAGE = 6

class TextNode():
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        text = repr(self.text)
        text_type = repr(self.text_type.name)  # Use the enum name for better readability
        url = repr(self.url)
        return f"TextNode({text}, {text_type}, {url})"