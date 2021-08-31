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

# 7.A. Lists: Pairs de nombres égaux

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), compter le nombre de pairs de nombres égaux. Chaque pair de deux nombres égaux devra être compté exactement une fois.

## Exemple d'entrée #1

```
1 2 3 2 3
```

## Exemple de sortie #1

```
2
```

## Exemple d'entrée #2

```
1 1 1 1 1
```

## Exemple de sortie #2

```
10
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

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
counter = 0
for i in range(len(a)):
  for j in range(i + 1, len(a)):
    if a[i] == a[j]:
      counter += 1
print(counter)
```
````
