class HTMLGen:
    @staticmethod
    def a(content):
        return f'<a>{content}</a>'
    
    @staticmethod
    def b(content):
        return f'<b>{content}</b>'
    
    @staticmethod
    def p(content):
        return f'<p>{content}</p>'
    
    @staticmethod
    def body(content):
        return f'<body>{content}</body>'
    
    @staticmethod
    def div(content):
        return f'<div>{content}</div>'
    
    @staticmethod
    def span(content):
        return f'<span>{content}</span>'
    
    @staticmethod
    def title(content):
        return f'<title>{content}</title>'
    
    @staticmethod
    def comment(content):
        return f'<!--{content}-->'