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

# 2.C. Nombres : cadran d'une horloge

## Consignes

L'aiguille des heures d'une horloge analogique a tourné de α degrés depuis minuit. Déterminer de combien de degrés l'aiguille des minutes a tourné depuis l'heure en cours. Les entrées et sorties de ce programme sont des entiers.

## Exemple d'entrée (angle en degrés de l'aiguille des heures)

```
190
```

(6h20)

## Exemple de sortie (angle en degrés de l'aiguille des minutes)

```
120
```

(20 min)

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
print(int(input()) % 30 * 12)
```
````
