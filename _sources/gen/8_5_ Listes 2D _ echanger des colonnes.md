# 8.5. Listes 2D : échanger des colonnes

## Consignes

Étant donnés deux entiers entrés au clavier - le nombre de lignes `m` et de colonnes `n` d'une liste 2D `m×n` - suivis de la saisie de `m` lignes de `n` entiers, puis de deux entiers non négatifs `i` et `j` plus petits que `n`, échanger les colonnes `i` et `j` de la liste 2D et afficher le résultat.

## Exemple d'entrée

```
3 4
11 12 13 14
21 22 23 24
31 32 33 34
0 1
```

## Exemple de sortie

```
12 11 13 14
22 21 23 24
32 31 33 34
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#lists

https://docs.python.org/fr/3.6/tutorial/datastructures.html#list-comprehensions

https://docs.python.org/fr/3.6/tutorial/datastructures.html#nested-list-comprehensions

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire une liste 2D d'entiers :
# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
# Afficher la valeur de a :
# print(a)
</py-repl>
<py-terminal id="my-terminal"></py-terminal>
<py-script>
from js import document as _DOC
def clear_term():
    ter = _DOC.getElementById("my-terminal").firstChild
    ter.innerHTML = ''
</py-script>
<button py-click="clear_term()" id="clear-terminal" class="py-button">Nettoyer la console de sortie</button>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
col1, col2 = [int(s) for s in input().split()]
for i in range(m):
  a[i][col1], a[i][col2] = a[i][col2], a[i][col1]
for line in a:
  print(*line)
```
````