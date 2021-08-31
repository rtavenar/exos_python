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

# 6.C. While: Deuxième plus grande valeur

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la deuxième plus grande valeur lue **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première ni en deuxième position).

## **Exemple d'entrée**

```
1
7
9
0
```

## Exemple de sortie

```
7
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
maximum = int(input())
second_maximum = int(input())
if second_maximum > maximum:
  second_maximum, maximum = maximum, second_maximum
a = -1
while a != 0:
  a = int(input())
  if a > maximum:
    second_maximum, maximum = maximum, a
  elif a > second_maximum:
    second_maximum = a
print(second_maximum)
```
````
