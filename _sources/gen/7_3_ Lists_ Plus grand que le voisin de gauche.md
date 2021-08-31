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

# 7.3. Lists: Plus grand que le voisin de gauche

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher tous les éléments qui sont plus grand que leur voisin de gauche.

## Exemple d'entrée

```
1 5 2 4 3
```

## Exemple de sortie

```
5 4
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
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
  if a[i - 1] < a[i]:
    print(a[i], end=' ')
```
````
