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

# 6.B. While: Plus grand que le précédent

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez le nombre de valeurs strictement plus grandes que leur prédécesseur lues **avant** de rencontrer un 0 (on supposera que le 0 ne se trouve pas en première position).

## **Exemple d'entrée**

```
1
2
3
4
5
0
```

## **Exemple de sortie**

```
4
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
prev = next = int(input())
counter = 0
while next != 0:
  if prev < next:
    counter += 1
  prev, next = next, int(input())
print(counter)
```
````
