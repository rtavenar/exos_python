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

# 8.1. Listes 2D : multiplicateur

## Consignes

Étant donnés deux entiers entrés au clavier - le nombre de lignes `m` et de colonnes `n` d'une liste 2D `m`×`n` - suivis de la saisie  de `m` lignes de `n` entiers et d'un dernier entier `c`, multiplier chaque élément de la liste 2D par `c` et afficher le résultat.

## Exemple d'entrée

```
3 4
11 12 13 14
21 22 23 24
31 32 33 34
2
```

## Exemple de sortie

```
22 24 26 28
42 44 46 48
62 64 66 68
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#lists

https://docs.python.org/fr/3.6/tutorial/datastructures.html#list-comprehensions

https://docs.python.org/fr/3.6/tutorial/datastructures.html#nested-list-comprehensions

## Squelette

```{code-cell} ipython3

# Lire une liste 2D d'entiers :
# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]
# Afficher la valeur de a :
# print(a)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
c = int(input())
for i in range(m):
  for j in range(n):
    a[i][j] *= c
for line in a:
  print(*line)
```
````
