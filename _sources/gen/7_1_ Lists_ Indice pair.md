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

# 7.1. Lists: Indice pair

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher tous les éléments ayant un indice pair (i.e. `A[0]`, `A[2]`, `A[4]`, ...).

## Exemple d'entrée

```
5 6 7 8 9
```

## Exemple de sortie

```
5 7 9
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
for i in a[::2]:
  print(i, sep=' ')
```
````
