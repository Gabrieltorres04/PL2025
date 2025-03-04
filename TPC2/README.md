# PL 24/25 - TPC2
## Análise de um dataset de obras musicais
### Problema
Deverás ler o dataset, processá-lo e criar os seguintes resultados:

1. Lista ordenada alfabeticamente dos compositores musicais;

2. Distribuição das obras por período: quantas obras catalogadas em cada período;

3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período


### Resolução
O programa desenvolvido para este exercício processa um dataset de obras musicais e gera três resultados:
 
1. **Lista Ordenada de Compositores Musicais:**  
   Extraímos os nomes dos compositores, eliminamos duplicados e ordenamos a lista alfabeticamente.

2. **Distribuição das Obras por Período:**  
   Verificamos, para cada período, quantas obras foram catalogadas. Essa contagem pode ser obtida ao verificar o tamanho da lista de obras associada a cada período.

3. **Dicionário de Obras por Período:**  
   Criamos um dicionário onde cada chave é um período e o valor associado é uma lista, em ordem alfabética, dos títulos das obras daquele período.

## Metodologia

### 1. Leitura e Agrupamento dos Registros CSV
- **Desafio:**  
  O arquivo CSV pode conter campos com quebras de linha dentro de aspas, o que faz com que um registro se estenda por várias linhas.

- **Solução:**  
  A função `read_csv_rows()` lê o arquivo linha a linha, acumulando as linhas até que o número de aspas (`"`) esteja balanceado (número par de aspas). Dessa forma, garantimos que cada registro completo seja processado corretamente, mesmo que contenha quebras de linha.

### 2. Parsing dos Campos do CSV
- **Desafio:**  
  Processar cada registro para separar os campos corretamente, lidando com delimitadores (`;`) e aspas que podem estar presentes para encapsular campos com caracteres especiais.

- **Solução:**  
  A função `parse_csv_line()` percorre cada caractere do registro e divide os campos de acordo com o delimitador, tomando cuidado para identificar quando o conteúdo está entre aspas, inclusive tratando aspas duplicadas para escapar aspas internas.

### 3. Processamento e Extração dos Dados Relevantes
- **Extração dos Compositores:**  
  Ao percorrer cada registro, o programa adiciona o nome do compositor (campo com índice 4) a uma lista. Após o processamento, esta lista é ordenada alfabeticamente.

- **Agrupamento das Obras por Período:**  
  Para cada registro, o título da obra (campo com índice 0) é adicionado a uma lista associada ao seu período (campo com índice 3). Se o período ainda não existir no dicionário, uma nova entrada é criada.

## Conclusão

Essa implementação demonstra como manipular entradas CSV não triviais sem recorrer à biblioteca padrão `csv`, tratando de registros com múltiplas linhas e campos complexos. O resultado é uma análise organizada do dataset, facilitando a obtenção de estatísticas como a distribuição das obras por período e uma consulta rápida aos nomes dos compositores.