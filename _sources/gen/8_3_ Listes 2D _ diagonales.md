# 8.3. Listes 2D : diagonales

## Consignes

Étant donné un entier `n` entré au clavier, créer puis afficher une liste 2D suivant les règles ci-dessous :

- Sur la diagonale principale mettre la valeur `0`.
- Sur les diagonales adjacentes à la principale, mettre la valeur `1`.
- Sur les diagonales suivantes mettre la valeur `2`, et ainsi de suite ...

## Exemple d'entrée

```
5
```

## Exemple de sortie

```
0 1 2 3 4
1 0 1 2 3
2 1 0 1 2
3 2 1 0 1
4 3 2 1 0
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
    # Lire un entier au clavier :
# a = int(input())
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
    a[i][j] = abs(i - j)
for line in a:
  print(*line)
```
````
