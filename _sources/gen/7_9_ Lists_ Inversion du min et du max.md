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

# 7.9. Lists: Inversion du min et du max

## Consigne

À partir d'une liste de nombres entiers distincts donnés en entrée (chaque nombre est séparé par un espace), inverser le minimum et le maximum et afficher la liste résultat.

## Exemple d'entrée

```
3 4 5 2 1
```

## Exemple de sortie

```
3 4 1 2 5
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

## Squelette

```{code-cell} ipython3

# Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
# print(a)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
pos_min = a.index(min(a))
pos_max = a.index(max(a))
a[pos_min], a[pos_max] = a[pos_max], a[pos_min]
print(*a)
```
````
