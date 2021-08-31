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

# 6.7. While: Moyenne d'une séquence

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la moyenne des valeurs lues **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première position).

## **Exemple d'entrée**

```
10
30
0
```

## **Exemple de sortie**

```
20.0
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

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
a = int(input())
length = 0
sum_of_sequence = 0
while a != 0:
  sum_of_sequence += a
  length += 1
  a = int(input())
print(sum_of_sequence / length)
```
````
