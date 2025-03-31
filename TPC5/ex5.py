import json
import sys
import re
import ply.lex as lex
from datetime import date

stock_items = {}

tokens = (
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SAIR"
    )

def t_LISTAR(t):
    r'LISTAR'
    return t
    
def t_SAIR(t):
    r'SAIR'
    return t
    
def t_MOEDA(t):
    r'MOEDA\s+((1e|2e|50c|20c|10c|5c|2c|1c),?\s*)+'
    return t
    
def t_SELECIONAR(t):
    r'SELECIONAR\s+[a-zA-Z0-9]+'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter inválido '{t.value[0]}' na posição {t.lexpos}")
    t.lexer.skip(1)


def listar():
    print('maq:')
    print('     Código      |                    Nome                     |   Quantidade   |    Preço    ')
    print('------------------------------------------------------------------------------------------------')
    for item in stock_items:
        cod = item["cod"]
        nome = item["nome"]
        quant = item["quant"]
        preco = item["preco"]
        print(f"{cod:^18}|{nome:^45}|{quant:^16}|{preco:^13.2f}")

def load_stock():
    global stock_items
    with open("stock.json", "r") as file:
        data = json.load(file)
        stock_items = data["stock"] 
    
def save_stock(stock):
    with open("stock.json", "w") as file:
        data = {"stock": stock}
        json.dump(data, file, indent=4)
    
def troco(saldo):
    coins = [2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    coin_names = ["2e", "1e", "50c", "20c", "10c", "5c", "2c", "1c"]
    
    result = []
    remaining = round(saldo, 2)   
    
    for i, coin_value in enumerate(coins):
        count = int(remaining / coin_value)
        if count > 0:
            result.append(f"{count}x{coin_names[i]}")
            remaining = round(remaining - count * coin_value, 2)
    
    if not result:
        return "0.00€"
    else:
        return f"{saldo:.2f}€: " + ", ".join(result)
    
def main():
    saldo = 0
    load_stock()
    lexer = lex.lex(reflags=re.IGNORECASE)
    print(f"maq: {date.today()} Stock carregado, Estado atualizado.")
    print("maq: Olá. Pode agora fazer o seu pedido.")
    
    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if token.type == "LISTAR":
                listar()
                
            elif token.type == "SELECIONAR":
                cod = token.value.split()[1]
                
                product = None
                for item in stock_items:
                    if item["cod"] == cod:
                        product = item
                        break
                if not product:
                    print(f"maq: Produto não encontrado.")
                    continue
                if saldo == 0:
                    print(f"maq: O Preço do produto é: {product['preco']:.2f}€")
                    continue
                if saldo < product["preco"]:
                    print(f"maq: Saldo insuficiente para satisfazer o seu pedido.")
                    print(f"maq: Saldo = {saldo:.2f}€ e Pedido = {product['preco']:.2f}€")
                    continue
                if product["quant"] == 0:
                    print(f"maq: Produto esgotado.")
                    continue
                
                product["quant"] -= 1
                saldo -= product["preco"]
                print(f"maq: Produto: {product['nome']} - {product['preco']:.2f}€")
                print(f"maq: Saldo restante: {saldo:.2f}€")

            elif token.type == "MOEDA":
                coins_part = token.value.split(None, 1)[1] 
                coins = re.findall(r'(1e|2e|50c|20c|10c|5c|2c|1c)', coins_part)

                added_value = 0
                for coin in coins:
                    if coin.endswith('e'):
                        added_value += float(coin[:-1])
                    elif coin.endswith('c'):
                        added_value += float(coin[:-1]) / 100

                saldo += added_value
                print(f"maq: Inseriu {added_value:.2f}€")
                print(f"maq: Saldo = {saldo:.2f}€")

            elif token.type == "SAIR":
                if saldo > 0:
                    print(f"maq: Pode retirar o troco: {troco(saldo)}")
                print("maq: Até à próxima.")
                save_stock(stock_items)
                exit(0)

if __name__ == "__main__":
    main()