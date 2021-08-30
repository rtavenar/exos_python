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

# 7.B. Lists: Element unique

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher les éléments qui n'apparaissent qu'une seule fois. De tels éléments devront être affiché dans l'ordre dans lequel ils apparaissent dans la liste originale. Vous pouvez utiliser la méthode count() (Cf. deuxième lien de l'aide ci-dessous).

## Exemple d'entrée

```
4 3 5 2 5 1 3 5
```

## Exemple de sortie

```
4 2 1
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
for i in a:
  if a.count(i) == 1:
    print(i, end=' ')
```
````
