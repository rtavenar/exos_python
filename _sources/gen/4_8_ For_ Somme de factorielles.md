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

# 4.8. For: Somme de factorielles

## Consigne

En mathématique, la factorielle d'un nombre entier **n** (**n!**) est le produit suivant :

n! = 1 × 2 × … × n


Pour le nombre entier donné n calculer la valeur

1! + 2! + 3! + ... + n!

Essayer de trouver la solution qui n'utilise qu'une seule boucle for. Ne pas utiliser le module math pour cet exercice.

## Exemple d'entrée

```
4
```

## Exemple de sortie

```
33
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} ipython3

# Read an integer:
# a = int(input())
# Print a value:
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
partial_sum = 0
current_factorial = 1
for i in range(1, int(input()) + 1):
  current_factorial *= i
  partial_sum += current_factorial
print(partial_sum)
```
````
