import re

class Lexer:
    def __init__(self, grammar, ignore):
        self.grammar = grammar
        self.ignore = ignore
        self.tokens = []
        
    def tokenize(self, code):
        self.tokens = []
        token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.grammar.items())
        for token in re.finditer(token_regex, code, re.DOTALL):
            if token.lastgroup not in self.ignore:
                if token.lastgroup == 'INTEGER':
                    value = int(token.group(0))
                elif token.lastgroup == 'FLOAT':
                    value = float(token.group(0))
                else:
                    value = token.group(0)
                if token.lastgroup not in ['SL_COMMENT', 'ML_COMMENT']:
                    self.tokens.append((token.lastgroup, value))

          
    def get_next_token(self):
        if self.tokens:
            return self.tokens.pop(0)
        else:
            return None
