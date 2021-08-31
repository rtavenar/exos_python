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

# 7.D. Lists: Bowling

## Consigne

Au bowling, le joueur commence avec 10 quilles alignées à l'extrémité d'une voie. Le but est de faire tomber toutes les quilles. Dans cet exercice, le nombre de quilles et de boules variera. On entrera au clavier le nombre de quilles N et le nombre de boules K à lancer sur une première ligne ("10 3" sur l'exemple ci-dessous), suivi de K paires de numéros (une pour chaque boule lancée : "8 10" est le premier lancé). Déterminez quelles quilles restent debout après que toutes les boules ont été lancées.


Les quilles sont numérotées de 1 à N. Les paires de numéros suivants chaque lancé (une pour chaque lancé), représentent la première et la dernière position (inclusive) des quilles qui ont été renversées à la suite de chaque lancé. Afficher une séquence de N caractères, où "I" représente une quille encore debout et "." représente une quille renversée.

## Exemple d'entrée

```
10 3
8 10
2 5
3 6
```

## Exemple de sortie

```
I.....I...
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
n, k = [int(s) for s in input().split()]
pins = ['I'] * n
for i in range(k):
  left, right = [int(s) for s in input().split()]
  for j in range(left - 1, right):
    pins[j] = '.'
print(''.join(pins))
```
````
