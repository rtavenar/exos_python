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

# 4.1. For: Series - 1

## Consigne

Soit deux entiers A et B (A ≤ B) donnés en entrée. Afficher tous les nombres de A à B bornes comprises.

## Exemple d'entrée

```
1
10
```

## Exemple de sortie

```
1 2 3 4 5 6 7 8 9 10
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Read an integer:
# a = int(input())
# Print a value:
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())

for i in range(a, b + 1):
  print(i, end=' ')
```
````
