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

# 2.A. Nombres : jour de la semaine

## Consignes

Les jours de la semaine sont numérotés de la manière suivantes : 0 —Dimanche, 1 — Lundi, 2 — Mardi, ..., 6 — Samedi. Le programme reçoit un entier _K_ compris entre 1 et 365. Trouver et afficher le numéro du jour de la semaine du _K_-ième jour de l'année sachant que le 1er janvier de cette année est un jeudi.


## Exemple d'entrée

```
1
```

## Exemple de sortie

```
4
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

## Squelette

```{code-cell} ipython3

# Lire un entier :
# a = int(input())
# Afficher la valeur de a :
# print(a)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print((int(input()) + 3) % 7)
```
````
