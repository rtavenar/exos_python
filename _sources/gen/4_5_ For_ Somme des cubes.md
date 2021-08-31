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

# 4.5. For: Somme des cubes

## Consigne

Pour un entier N donné en entrée, calculer la somme suivante :

1³ + 2³ + ... + N³

## Exemple d'entrée

```
3
```

## Exemple de sortie

```
36
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Read an integer:
# a = int(input())
# Print a value:
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
result = 0
for i in range(1, int(input()) + 1):
  result += i ** 3
print(result)
```
````
