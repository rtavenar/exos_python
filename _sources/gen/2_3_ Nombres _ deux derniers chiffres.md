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

# 2.3. Nombres : deux derniers chiffres

## Consignes

Étant donné un entier supérieur à 9, afficher ses deux derniers chiffres.

## Exemple d'entrée

```
1234
```

## Exemple de sortie

```
34
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lire un entier :
# a = int(input())
# Afficher la valeur de a :
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print(a % 100)
```
````
