import re
import ply.lex as lex
import sys

reserved = {
    'select':'SELECT',
    'where':'WHERE',
    'LIMIT':'LIMIT'
}

tokens = [
    'LCBRACES',
    'RCBRACES',
    'DOT',
    'VAR',
    'IDENTIFIER',
    'STRING',
    'LANGTAG',
    'NUMBER'
] + list(reserved.values())

t_LCBRACES = r'\{'
t_RCBRACES = r'\}'
t_DOT = r'\.'
t_ignore = ' \t'
t_NUMBER = r'[0-9]+'

def t_VAR(t):
    r'\?\w+'
    t.value = t.value[1:] # Remover o '?' do inicio
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*(?::[a-zA-Z0-9_]+)?'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')  # Check for reserved words
    return t

def t_STRING(t):
    r'\".*\"'
    t.value = t.value[1:-1]
    return t

def t_LANGTAG(t):
    r'@\w+'
    t.value = t.value[1:]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)    

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":    
    s = sys.stdin.read()
    lexer.input(s)
    for tok in iter(lexer.token, None):
        print(tok)   
    