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

# 3.1. If/else: Pair ou impair

## Consigne

Étant donné un entier, afficher "pair" s'il est pair ou "impair" sinon.

## Exemple d'entrée #1

```
5
```

## Exemple de sortie #1

```
impair
```

## Exemple d'entrée #2

```
6
```

## Exemple de sortie #2

```
pair
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Squelette

```{code-cell} ipython3

# Lire un entier
# a = int(input())
# Afficher une valeur:
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
if int(input()) % 2 == 0:
  print('pair')
else:
  print('impair')
```
````
