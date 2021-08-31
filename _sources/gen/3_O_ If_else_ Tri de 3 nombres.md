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

# 3.O. If/else: Tri de 3 nombres

## **Énoncé**

Étant donnés 3 entiers, les afficher dans l'ordre croissant.

## Example input

```
5
3
7
```

## Example output

```
3
5
7
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

if a <= b <= c:
  print(a, b, c, end='\n')
elif a <= c <= b:
  print(a, c, b, end='\n')
elif b <= a <= c:
  print(b, a, c, end='\n')
elif b <= c <= a:
  print(b, c, a, end='\n')
elif c <= a <= b:
  print(c, a, b, end='\n')
else:
  print(c, b, a, end='\n')
```
````