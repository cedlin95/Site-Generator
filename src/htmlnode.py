
class HTMLNODE():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None or not self.props:
            return ""

        prop_string = ""
        for key,value in self.props.items():
            prop_string +=f' {key}="{value}"' 
        return prop_string
    
    def __repr__(self):
        return (f"HTMNNode({self.tag},{self.value},{self.children}, {self.props})")
        