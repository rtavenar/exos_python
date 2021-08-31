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

# 4.A. For: Echelle

## Consigne

Pour une valeur entière n ≤ 9 afficher une échelle de n étapes. La k-ième étape correspond aux entiers de 1 à k sans espace entre eux.

Pour faire cela, vous pouvez utiliser l'argument end de la fonction print().


## Exemple d'entrée

```
3
```

## Exemple de sortie

```
1
12
123
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

https://docs.python.org/fr/3/library/functions.html#print

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
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print(j, end='')
  print()
```
````
