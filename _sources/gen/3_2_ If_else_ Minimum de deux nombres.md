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

# 3.2. If/else: Minimum de deux nombres

## Consigne

Étant donnés 2 entiers, affichez le plus petit des deux

## Exemple d'entrée

```
3
7
```

## Exemple de sortie

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Squelette

```{code-cell} ipython3

# Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())
if a < b:
  print(a)
else:
  print(b)
```
````
