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

# 6.1. While: Liste des carrés

## Énoncé

Pour un entier N donné, affichez (dans l'ordre) tous les carrés d'entiers positifs inférieurs ou égaux à N.

## Exemple d'entrée

```
50
```

## **Exemple de sortie**

```
1 4 9 16 25 36 49
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

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
n = int(input())
i = 1
while i ** 2 <= n:
  print(i ** 2, end=' ')
  i += 1
```
````
