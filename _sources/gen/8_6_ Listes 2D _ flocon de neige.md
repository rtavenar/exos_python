# 8.6. Listes 2D : flocon de neige

## Consignes

Étant donné un entier impair positif `n` entré au clavier, créer une liste 2D de taille `n×n`. Remplir chaque élément de cette liste 2D avec le caractère "`.`". Ensuite, remplir la ligne du milieu, la colonne du milieu et la première diagonale avec le caractère `"*"`.  Vous obtiendrez l'image d'un flocon de neige. Afficher le flocon de neige à partir des éléments de la liste 2D `n×n` et séparer les caractères par un simple espace.

## Exemple d'entrée

```
7
```

## Exemple de sortie

```
* . . * . . *
. * . * . * .
. . * * * . .
* * * * * * *
. . * * * . .
. * . * . * .
* . . * . . *
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
a = [['.'] * n for i in range(n)]
for i in range(n):
  for j in range(n):
    if i == j or i + j + 1 == n or i == n // 2 or j == n // 2:
      a[i][j] = '*'
for line in a:
  print(*line)
```
````