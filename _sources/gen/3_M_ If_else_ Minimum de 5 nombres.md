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

# 3.M. If/else: Minimum de 5 nombres

## **Énoncé**

Étant donnés 5 nombres, afficher leur minimum.

## Exemple d'entrée

```
10
20
30
40
50
```

## Exemple de sortie

```
10
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
least = int(input())

new_integer = int(input())
if new_integer < least:
  least = new_integer

new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
print(least)
```
````
