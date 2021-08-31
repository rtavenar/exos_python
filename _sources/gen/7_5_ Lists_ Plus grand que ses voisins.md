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

# 7.5. Lists: Plus grand que ses voisins

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), déterminer et afficher le nombre d'éléments plus grands que leurs deux voisins.

Le premier et le dernier éléments de  la liste ne doivent pas être considérés car ils n'ont qu'un seul voisin.

## Exemple d'entrée

```
1 5 1 5 1
```

## Exemple de sortie

```
2
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
for i in range(1, len(a) - 1):
  if a[i - 1] < a[i] > a[i + 1]:
    counter += 1
print(counter)
```
````
