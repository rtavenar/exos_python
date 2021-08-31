---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

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

## Squelette

```{code-cell} ipython3

# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
for i in range(0, len(a) - 1, 2):
  a[i], a[i + 1] = a[i + 1], a[i]
print(' '.join([str(elem) for elem in a]))
```
````
