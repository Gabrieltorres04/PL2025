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
