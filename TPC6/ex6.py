import ply.lex as lex
import sys
import re

tokens = (
    "NUM", 
    "PLUS",
    "MINUS",
    "MULT",
    "DIV",
    "OPAR",
    "CPAR"
)



t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_OPAR = r'\('
t_CPAR = r'\)'

def t_NUM (t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t\n"

def t_error(t):
    print("Invalid character:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize(data):
    lexer.input(data)
    return list(iter(lexer.token, None))

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def match(self, token_type):
        token = self.current_token()
        if token and token.type == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Esperava {token_type}, mas encontrou {token.type if token else 'EOF'}")

    def parse(self):
        result = self.expr()
        if self.current_token() is not None:
            raise SyntaxError("Token inesperado após o final da expressão")
        return result

    # expr -> term ((PLUS | MINUS) term)*
    def expr(self):
        value = self.term()
        while True:
            token = self.current_token()
            if token and token.type in ("PLUS", "MINUS"):
                op = token.type
                self.match(op)
                right = self.term()
                if op == "PLUS":
                    value += right
                else:
                    value -= right
            else:
                break
        return value

    # term -> factor ((MULT | DIV) factor)*
    def term(self):
        value = self.factor()
        while True:
            token = self.current_token()
            if token and token.type in ("MULT", "DIV"):
                op = token.type
                self.match(op)
                right = self.factor()
                if op == "MULT":
                    value *= right
                else:
                    value /= right  
            else:
                break
        return value

    # factor -> NUM | OPAR expr CPAR
    def factor(self):
        token = self.current_token()
        if token is None:
            raise SyntaxError("Esperava número ou '(' mas encontrou EOF")
        
        if token.type == "NUM":
            self.match("NUM")
            return token.value
        elif token.type == "OPAR":
            self.match("OPAR")
            value = self.expr()
            self.match("CPAR")
            return value
        else:
            raise SyntaxError(f"Token inesperado: {token.type}")

if __name__ == "__main__":
    data = sys.stdin.read().strip()
    if not data:
        print("Nenhuma entrada fornecida.")
        sys.exit(1)
    
    tokens_list = tokenize(data)
    parser = Parser(tokens_list)
    try:
        resultado = parser.parse()
        print("Resultado da expressão:", resultado)
    except SyntaxError as e:
        print("Erro de sintaxe:", e)