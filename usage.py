from pyLITE import Lexer

# Define your grammar and ignore characters. Pretty easy, just look up regex
grammar = {
    'SL_COMMENT': r'\/\/[^\n]*',  # Single-line comment. Syntax: // hi
    'ML_COMMENT': r'\/\*.*?\*\/',  # Multi-line comment. Syntax: /* hi */
    'WHILE': r'while', # while
    'DO': r'do', # do
		'FOR': r'for', # for
    'IN': r'in', # in
    'TO': r'\.\.\.', # ... (to)
    'FUN': r'fun', # fun
    'HAS': r'has', # has (parameter def in this sample)
    'WRITE': r'write', # write (print)
    'VAR': r'var', # var
    'GETS': r'gets', # gets (syntax: var foo gets "bar")
    'END': r'end', # end
    'IF': r'if', # if
    'EQUALS': r'eq', # eq
    'NOTEQUALS': r'!eq', # !eq
    'LESSTHAN': r'less', # less
    'MORETHAN': r'more', # more
    'THEN': r'then', # then (syntax: if foo eq "bar" then)
    'STRING': r'"[^"]*"', # string ("anything in quotes")
    'FLOAT': r'\d+\.\d+|\d+\.', # float
    'INTEGER': r'\d+', # integer
    'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9]*', # identifier (variable/function)
    'PLUS': r'\+', # +
    'MINUS': r'-', # -
    'TIMES': r'\*', # *
    'DIVIDE': r'/', # /
    'MODULO': r'%', # %
    'LPAREN': r'\(', # (
    'RPAREN': r'\)', # )
    'COMMA': r',', # ,
    'COLON': r':', # :
}
ignore = " \t\n" # Ignoring whitespace, aka it won't count as a token

# Create an instance of the Lexer class
lexer = Lexer(grammar=grammar, ignore=ignore)

# Tokenize input code
code = """
var foo gets 1.5
"""
lexer.tokenize(code)

token = lexer.get_next_token()
while token != None:
    print(token) # Do something with the token
    token = lexer.get_next_token()
