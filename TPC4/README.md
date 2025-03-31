# PL 24/25 - TPC 4

## Analisador Léxico

### Problema:
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:
```SPARQL
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000

```

### Resolução
O programa desenvolvido para o TPC4 implementa um analisador léxico para uma linguagem de query, permitindo a identificação de diferentes tokens presentes nas frases escritas no formato proposto (similar a SPARQL). A seguir, detalhamos os passos principais da implementação:

1. **Definição dos Tokens e Palavras Reservadas:**  
   Foram definidos os tokens básicos (como `{`, `}`, `.`, variáveis, identificadores, strings, language tags e números) e um dicionário de palavras reservadas (ex.: `select`, `where`, `LIMIT`). Isso permite que alguns identificadores sejam automaticamente convertidos para os seus respetivos tokens reservados ao serem reconhecidos.

2. **Especificação dos Padrões com Expressões Regulares:**  
   Cada token possui uma expressão regular associada (por exemplo, para variáveis iniciadas por `?`, ou para strings delimitadas por aspas) que possibilita seu reconhecimento no texto de entrada.  
   - A função `t_VAR` processa os tokens de variável, removendo o caráter `?` do início.  
   - A função `t_IDENTIFIER` identifica nomes (e situações com namespace, separados por `:`) e verifica se correspondem a palavras reservadas.  
   - Outros tokens, como `LCBRACES`, `RCBRACES`, `DOT` e `NUMBER`, contam também com expressões regulares específicas.

3. **Tratamento de Caracteres Desconhecidos e Quebras de Linha:**  
   Funções específicas, como `t_error` e `t_newline`, lidam com caracteres inválidos (imprimindo uma mensagem e ignorando-os) e atualizam o número de linhas conforme necessário, garantindo um rastreamento correto do posicionamento dos tokens.

4. **Integração com PLY para Montagem do Analisador:**  
   Utilizando a biblioteca PLY (Python Lex-Yacc), o programa compila as especificações lexicas e constrói um lexer capaz de processar a entrada.  
   - A entrada é lida a partir da entrada padrão (`stdin`), permitindo testar o analisador via redirecionamento de ficheiros ou entrada direta no terminal.  
   - Cada token identificado é impresso, facilitando a verificação do funcionamento do analisador.
