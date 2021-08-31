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

# 2.1. Nombres : deux chiffres

## Consignes

Étant donné un entier à deux chiffres, afficher son premier chiffre (dizaines) puis son deuxième chiffre (unités). Utiliser l'opérateur de division entière pour obtenir le chiffre des dizaines et l'opérateur de modulo (reste de la division entière) pour obtenir le chiffre des unités.

## Exemple d'entrée

```
79
```

## Exemple de sortie

```
7 9
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

## Squelette

```{code-cell} ipython3

# Lire un entier :
# a = int(input())
# Afficher la valeur de a :
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print(a // 10, a % 10)
```
````
