# PL 24/25 - TPC3
## Conversor de MarkDown para HTML
### Problema
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet

### Resolução

O programa desenvolvido para o TPC3 converte um texto em Markdown para HTML, abrangendo vários elementos essenciais da sintaxe Markdown. A seguir, uma breve descrição dos passos implementados:

1. **Conversão de Cabeçalhos (Headers):**  
   São identificadas linhas que começam com `#` para serem transformadas nas tags HTML correspondentes (`<h1>` a `<h6>`), de acordo com o número de `#` presentes. Essa transformação é realizada utilizando expressões regulares que contam as ocorrências e geram a tag apropriada.

2. **Formatação de Negrito e Itálico:**  
   - **Negrito:** Textos delimitados por `**` são convertidos para a tag `<b>`.  
   - **Itálico:** Textos delimitados por `*` são convertidos para a tag `<i>`.  
     
   O uso de expressões regulares permite identificar e substituir esses padrões de forma eficaz.

3. **Conversão de Listas Ordenadas:**  
   A função `convert_ordered_lists()` percorre o texto procurando por itens de lista ordenada (padrão numérico seguido de ponto).  
   - Ao identificar o início de uma lista, inicia-se a tag `<ol>` e cada item é encapsulado com a tag `<li>`.  
   - Quando a sequência numérica não é mais detectada, a lista é encerrada com `</ol>`, garantindo a correta estruturação do HTML.

4. **Conversão de Links e Imagens:**  
   São aplicadas expressões regulares para transformar a sintaxe dos links (ex.: `[texto](link)`) e das imagens (ex.: `![texto](link)`) nas tags HTML correspondentes:  
   - **Links:** São convertidos para `<a href="link">texto</a>`.  
   - **Imagens:** São convertidas para `<img src="link" alt="texto" />`.

Esta abordagem modular não só implementa a conversão dos elementos básicos da sintaxe Markdown como também facilita a expansão do conversor para suportar novos elementos ou aprimoramentos futuros.