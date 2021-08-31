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

## Squelette

```{code-cell} ipython3

# Lire un entier au clavier :
# a = int(input())
# Afficher la valeur de a :
# print(a)
```

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
