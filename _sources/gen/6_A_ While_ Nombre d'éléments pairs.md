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

# 6.A. While: Nombre d'éléments pairs

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez le nombre de valeurs paires lues **avant** de rencontrer un 0.

## **Exemple d'entrée**

```
2
1
4
0
```

## **Exemple de sortie**

```
2
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

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
a = int(input())
num_even = 0
while a != 0:
  if a % 2 == 0:
    num_even += 1
  a = int(input())
print(num_even)
```
````
