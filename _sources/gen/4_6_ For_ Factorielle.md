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

# 4.6. For: Factorielle

## Consigne

En mathématique, la factorielle d'un entier n (n!) est le produit suivant :

n! = 1 × 2 × … × n

Pour l'entier n donné en entrée, calculer la valeur de **n!**. Ne pas utiliser le module math dans cet exercice.

## Exemple d'entrée

```
4
```

## Exemple de sortie

```
24
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} python
# Read an integer:
# a = int(input())
# Print a value:
# print(a)
```

````{dropdown} Proposition de solution

```python
result = 1
for i in range(1, int(input()) + 1):
  result *= i
print(result)
```
````
