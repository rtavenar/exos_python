# 7.7. Lists: Inversion des voisins

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), inverser la place de chaque pair d'élément adjacent (inverser A[0] avec A[1], A[2] avec A[3], etc.). Afficher la liste résultat. Si la liste de départ contient un nombre impair d'éléments, laisser le dernier élément en dernière position.

## Exemple d'entrée

```
1 2 3 4 5
```

## Exemple de sortie

```
2 1 4 3 5
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
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
a = [int(s) for s in input().split()]
for i in range(0, len(a) - 1, 2):
  a[i], a[i + 1] = a[i + 1], a[i]
print(' '.join([str(elem) for elem in a]))
```
````
