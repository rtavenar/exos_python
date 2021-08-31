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

# 4.4. For: Somme de N nombres

## Consigne

N nombres sont donnés en entrés. Lire chaque nombre et afficher la leur somme.

Le premier nombre entré est un entier N, qui est le nombre d'entiers qui seront entrés. Chacune des N entrées contient un entier. Afficher la somme de ces N entiers.


## Exemple d'entrée

```
10
1
2
1
1
1
1
3
1
1
1
```

## Exemple de sortie

```
13
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
  result += int(input())
print(result)
```
````
