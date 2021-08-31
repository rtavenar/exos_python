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

# 4.2. For: Series - 2

## Consigne

Soit deux entiers A et B donnés en entrée. Afficher tous les nombres de A à B bornes comprises, par ordre croissant, si A < B ou par ordre décroissant si A ≥ B.

## Exemple d'entrée

```
8
5
```

## Exemple de sortie

```
8 7 6 5
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} ipython3

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

if a < b:
  for i in range(a, b + 1):
    print(i, end=' ')
else:
  for i in range(a, b - 1, -1):
    print(i, end=' ')
```
````
