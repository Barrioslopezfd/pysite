class HTMLNode():
    def __init__(self,
                 tag:str|None = None,
                 value:str|None = None,
                 children:list['HTMLNode']|None = None,
                 props:dict|None = None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

    def to_html(self):
        raise NotImplementedError('am not an implemented boi')

    def props_to_html(self):
        if self.props == None:
            return ""

        attr=''

        for key, value in self.props.items():
            attr += f' {key}="{value}"'
        return attr

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict | None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        aux = ''
        if self.value == None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag == None or '':
            return f'{self.value}'
        elif self.props is not {} and self.props is not None:
            for key, value in self.props.items():
                aux=f'{aux} {key}="{value}"'
        return f"<{self.tag}{aux}>{self.value}</{self.tag}>"




