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

# 7.2. Lists: Element pair

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), afficher tous les éléments pairs. Utiliser une boucle for qui va itérer sur la liste et pas sur les indices. Autrement dit, ne pas utiliser range( )

## Exemple d'entrée

```
1 2 2 3 3 3 4
```

## Exemple de sortie

```
2 2 4
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#les-listes

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

## Squelette

```{code-cell} python
# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
```

````{dropdown} Proposition de solution

```python
a = [int(s) for s in input().split()]
for i in a:
  if i % 2 == 0:
    print(i, end=' ')
```
````
