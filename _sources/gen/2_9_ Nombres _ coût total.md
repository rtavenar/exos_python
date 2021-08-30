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

# 2.9. Nombres : coût total

## Consignes

Un gâteau coûte _A_ euros et _B_ centimes. Déterminer combien d'euros et de centimes on doit payer pour _N_ gâteaux. Le programme reçoit trois nombres entrés au clavier : _A_, _B_, _N_. Il doit afficher deux nombres : le coût total en euros et centimes.

## Exemple d'entrées

```
10
15
2
```

## Exemple de sortie

```
20 30
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

## Squelette

```{code-cell} python
# Lire un entier :
# a = int(input())
# Afficher la valeur de a :
# print(a)
```

````{dropdown} Proposition de solution

```python
item_dollars = int(input())
item_cents = int(input())
n = int(input())
total_cents = (item_dollars * 100 + item_cents) * n
print(total_cents // 100, total_cents % 100)
```
````
