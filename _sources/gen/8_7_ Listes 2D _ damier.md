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

# 8.7. Listes 2D : damier

## Consignes

Étant donnés deux entiers positifs `n` et `m` entrés au clavier, créer une liste 2D de taille `n×m` et la remplir avec les caractères "`.`" et "`*`" alternés en ligne et en colonne afin d'obtenir un motif en damier. Le coin haut gauche du damier doit contenir le caractère "`.`" .

## Exemple d'entrée

```
6 8
```

## Exemple de sortie

```
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#lists

https://docs.python.org/fr/3.6/tutorial/datastructures.html#list-comprehensions

https://docs.python.org/fr/3.6/tutorial/datastructures.html#nested-list-comprehensions

## Squelette

```{code-cell} ipython3

# Lire une liste d'entiers :
# a = [int(s) for s in input().split()]
# Afficher la valeure de a :
# print(a)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
n, m = [int(s) for s in input().split()]
a = [['.' if (i + j) % 2 == 0 else '*']
     for i in range(n)
     for j in range(m)]
for line in a:
  print(*line)
```
````
