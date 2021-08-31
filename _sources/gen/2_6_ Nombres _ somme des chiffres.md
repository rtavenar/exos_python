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

# 2.6. Nombres : somme des chiffres

## Consigne

Étant donné un entier à trois chiffres, calculer et afficher la somme de ses chiffres.

## Exemple d'entrée

```
123
```

## Exemple de sortie

```
6
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
print(a // 100 + a // 10 % 10 + a % 10)
```
````
