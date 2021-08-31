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

# 6.6. While: Somme d'une séquence

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez la somme des valeurs lues **avant** de rencontrer un 0.


## **Exemple d'entrée**

```
1
7
9
0
```

## **Exemple de sortie**

```
17
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
a = int(input())
sum_of_sequence = 0
while a != 0:
  sum_of_sequence += a
  a = int(input())
print(sum_of_sequence)
```
````
