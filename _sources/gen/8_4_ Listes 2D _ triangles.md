# 8.4. Listes 2D : triangles

## Consignes

Étant donné un entier `n` entré au clavier, créer et afficher une liste 2D de taille `n×n` suivant les règles ci-dessous :


- Sur l'anti-diagonale, mettre la valeur `1`.
- Sur les diagonales au dessus mettre la valeur `0`.
- Sur les diagonales en dessous mettre la valeur 2.

## Exemple d'entrée

```
4
```

## Exemple de sortie

```
0 0 0 1
0 0 1 2
0 1 2 2
1 2 2 2
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
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
  for j in range(n):
    if i + j + 1 < n: 
      a[i][j] = 0
    elif i + j + 1 == n:
      a[i][j] = 1
    else:
      a[i][j] = 2
for line in a:
  print(*line)
```
````