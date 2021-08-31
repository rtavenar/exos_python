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

# 3.8. If/else: Minimum de 3 nombres

## **Énoncé**

Étant donnés trois entiers, affichez le plus petit des 3.

## Exemple d'entrée

```
5
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
c = int(input())

if a < b and a < c:
  print(a)
elif b < a and b < c:
  print(b)
else:
  print(c)
```
````
