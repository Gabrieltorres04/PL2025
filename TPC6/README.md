# PL 24/25 - TPC6

## Analisador Sintático de Expressões Matemáticas

### Problema
Construir um analisador sintático para expressões aritméticas simples. O analisador deverá:
- Reconhecer números e operadores aritméticos: soma (`+`), subtração (`-`), multiplicação (`*`) e divisão (`/`)
- Suportar agrupamento de expressões usando parênteses
- Avaliar a expressão e computar o respetivo resultado
- Reportar erros de sintaxe quando a entrada não corresponder à gramática definida

### Resolução
Para a implementação deste exercício foi utilizada a biblioteca PLY . Os principais componentes são:

1. **Definição dos Tokens:**  
   Foram definidos os tokens necessários para identificar os componentes das expressões:
   - **NUM:** Números inteiros
   - **PLUS, MINUS, MULT, DIV:** Operadores aritméticos
   - **OPAR, CPAR:** Parênteses de abertura e de fechamento

2. **Analisador Léxico:**  
   O lexer utiliza expressões regulares para reconhecer os tokens a partir da entrada, ignorando espaços, tabulações e quebras de linha.  
   - Um método `t_error` foi definido para tratar caracteres inválidos.

3. **Parser com Análise Sintática:**  
   O parser implementa uma gramática simples para expressões aritméticas utilizando métodos recursivos:
   - **expr:** Responsável por operações de soma e subtração
   - **term:** Trata de operações de multiplicação e divisão
   - **factor:** Lida com números e expressões parentizadas
   - Durante a análise, o parser computa o valor da expressão e verifica a sintaxe, lançando exceções em caso de erros.

4. **Tokenização e Integração:**  
   A função `tokenize` processa a entrada e gera uma lista dos tokens reconhecidos. Em seguida, o objeto `Parser` utiliza essa lista para construir e avaliar o resultado da expressão.

