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

# 2.4. Nombres : chiffre des dizaines

## Consignes

Étant donné un entier, afficher son chiffre des dizaines.

## Exemple d'entrée

```
1234
```

## Exemple de sortie

```
3
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
print(int(input()) % 100 // 10)
```
````
