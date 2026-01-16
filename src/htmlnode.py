class HTMLNode():
    def __init__(self, tag, value="", children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("This method should be overridden by child classes.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        attributes = [f' {key}="{value}"' for key, value in self.props.items()]
        return "".join(attributes)

    def __repr__ (self):
        children_repr = ", ".join(repr(child) for child in self.children)

        props_repr = f"{{'{self.tag}': {{}}}}" if not self.props else str(self.props)

        return (f"HTMLNode(tag='{self.tag}', value='{self.value}', "
                f"children=[{children_repr}], props={props_repr})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
        if self.children:
            raise ValueError("LeafNode should not have any children.")

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")

        if self.tag is None:
            return self.value
        
        # Constructing the HTML string with attributes
        #attrs = ' '.join(f'{k}="{v}"' for k, v in self.props.items())
        props = self.props_to_html()

        if not props:
            html_content = f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            html_content = f'<{self.tag} {props}>{self.value}</{self.tag}>'

        return html_content

    def __repr__(self):
        # Similar to HTMLNode's __repr__ but doesn't include children
        return (f"{self.__class__.__name__}(tag={self.tag}, value={self.value}, "
                f"props={self.props})")

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
