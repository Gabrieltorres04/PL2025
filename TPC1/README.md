# PL 24/25 - TPC1
## Somador ON/OFF
### Problema
Criar um programa em python que:

 1. Some todas as sequências de dígitos num texto;
 2. Sempre que encontrar a string `Off`, em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é desligado;
 3. Sempre que encontrar a string `On`, em qualquer combinação de maiúsculas e minúsculas, o comportamento de soma é ligado;
 4. Sempre que encontrar o caráter `=`, o resultado da soma é colocado na saída.

### Resolução
O programa implementa um "Somador ON/OFF" que processa uma entrada de texto (via stdin) para realizar operações de soma condicional, de acordo com os seguintes critérios:

1. **Soma de Números**  
   O programa percorre cada caráter da entrada, identificando sequências de dígitos que, quando encontradas, são convertidas em números inteiros  e somadas ao resultado acumulado – mas apenas se o somador estiver ligado (modo ON).

2. **Comando ON/OFF**  
   - Ao encontrar a string `On` (em qualquer combinação de letras maiúsculas/minúsculas), o programa ativa o somador e passa a incluir os números encontrados na soma.  
   - Ao encontrar a string `Off` (em qualquer combinação de letras), o somador é desligado, fazendo com que novos números não sejam somados até que seja reativado.

3. **Exibição do Resultado**  
   Sempre que o programa encontra o caráter `=`, ele imprime o valor atual da soma acumulada.

### Metodologia de Implementação

- **Leitura da Entrada:**  
  O programa utiliza um loop que percorre cada linha recebida pela entrada padrão (`sys.stdin`), permitindo o processamento contínuo.

- **Análise caráter a caráter:**  
  Em vez de separar a entrada por espaço, o programa percorre cada linha caracter por caracter. Isso garante que números e comandos embutidos na mesma linha (como em "123Off456=789") sejam corretamente identificados e processados.


- **Processamento de Comandos e Valores:**  
  Ao percorrer uma linha:
  - Sequências numéricas são convertidas em inteiros (considerando sinal, se presente) e adicionadas a `result`, desde que `active` esteja True.
  - Comandos de ativação (`on`) e desativação (`off`) são identificados independentemente da capitalização, usando a função `lower()`.
  - Quando o caráter `=` é encontrado, o valor atual de `result` é impresso na saída.

