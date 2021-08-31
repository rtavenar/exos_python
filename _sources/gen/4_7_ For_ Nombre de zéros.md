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

# 4.7. For: Nombre de zéros

## Consigne

Soit N nombres : le premier nombre donné en entrée est N, après cela N entiers sont entrés. Compter le nombre de zéros parmi les entiers donnés et afficher le résultat.

Vous devez compter le nombre d'entiers égaux à zéro, mais pas le nombre de zéro qui compose un entier.


## Exemple d'entrée

```
5
0
700
0
200
2
```

## Exemple de sortie

```
2
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} ipython3

# Read an integer:
# a = int(input())
# Print a value:
# print(a)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
result = 0
for i in range(int(input())):
  if int(input()) == 0:
    result += 1
print(result)
```
````
