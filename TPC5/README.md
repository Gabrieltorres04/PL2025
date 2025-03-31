# PL 24/25 - TPC5

## Simulador de Máquina de Vending

### Problema
Construir um simulador de uma máquina de vending que aceite comandos através de um analisador léxico, permitindo:
- Listar produtos disponíveis
- Inserir moedas
- Selecionar produtos para compra
- Finalizar a operação com devolução do troco

### Resolução
O programa desenvolvido para este exercício simula uma máquina de vending utilizando um analisador léxico para processar comandos de entrada. Eis os principais componentes implementados:

1. **Analisador Léxico com PLY:**  
   Utilizou-se a biblioteca PLY (Python Lex-Yacc) para criar um analisador léxico que identifica quatro tipos de comandos:
   - **LISTAR:** Exibe todos os produtos disponíveis na máquina
   - **MOEDA:** Permite inserir dinheiro no formato `1e`, `2e`, `50c`, etc.
   - **SELECIONAR:** Permite escolher um produto pelo seu código
   - **SAIR:** Encerra a operação e devolve o troco

2. **Gestão de Stock:**  
   O sistema carrega e manipula dados de um ficheiro JSON que contém informações sobre os produtos disponíveis:
   - Código, nome, quantidade e preço de cada produto
   - Atualização dinâmica do stock quando um produto é comprado
   - Persistência dos dados (salvamento das alterações no ficheiro)

3. **Processamento de Moedas:**  
   Implementou-se um sistema para:
   - Reconhecer e validar os diferentes tipos de moedas (euros e cêntimos)
   - Acumular o saldo inserido pelo utilizador
   - Calcular e devolver o troco de forma otimizada, utilizando o menor número possível de moedas

4. **Interface com o Utilizador:**  
   O programa oferece feedback claro durante a interação:
   - Apresenta tabelas formatadas com informações dos produtos
   - Exibe mensagens informativas sobre saldo, preços e operações realizadas
   - Gere casos de erro (produto inexistente, saldo insuficiente, etc.)

5. **Cálculo de Troco:**  
   Ao finalizar a operação, o sistema:
   - Calcula o troco utilizando um algoritmo guloso (greedy)
   - Seleciona as moedas de maior valor primeiro para minimizar o número total
   - Apresenta o troco de forma legível (ex: "3.75€: 1x2e, 1x1e, 1x50c, 1x20c, 1x5c")

Esta implementação demonstra a aplicação de análise léxica em um contexto prático, além de trabalhar com persistência de dados, formatação de saída e algoritmos de otimização para o cálculo de troco.