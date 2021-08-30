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

# 2.5. Nombres : premier chiffre après la virgule

## Consignes

Etant donné un nombre réel positif, afficher son premier chiffre après la virgule (point décimal).

## Exemple d'entrée

```
1.79
```

## Exemple de sortie

```
7
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

## Squelette

```{code-cell} python
# Lire un entier :
# a = float(input())
# Afficher la valeur de a :
# print(a)
```

````{dropdown} Proposition de solution

```python
print(int(float(input()) * 10) % 10)
```
````
