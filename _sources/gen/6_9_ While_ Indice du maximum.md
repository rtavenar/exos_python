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

# 6.9. While: Indice du maximum

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la position de la première occurrence du maximum des valeurs lues **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première position).

## **Exemple d'entrée**

```
1
7
9
```

```
5
0
```

## **Exemple de sortie**

```
3
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#boucles-while

## Squelette

```{code-cell} python
# Read an integer:
# a = int(input())
# Print a value:
# print(a)
```

````{dropdown} Proposition de solution

```python
maximum = a = int(input())
maximum_index = 1
i = 1
while a != 0:
  a = int(input())
  i += 1
  if a > maximum:
    maximum = a
    maximum_index = i
print(maximum_index)
```
````
