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

# 7.8. Lists: Maximum

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver le premier élément maximum de la liste. Afficher sa valeur et son index (le premier élément porte l'index 0).

## Exemple d'entrée

```
1 2 3 2 1
```

## Exemple de sortie

```
3 2
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#les-listes

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

## Squelette

```{code-cell} python
# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
```

````{dropdown} Proposition de solution

```python
a = [int(s) for s in input().split()]
print(max(a), a.index(max(a)))
```
````
