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

# 3.5. If/else: Un seul positif

## **Énoncé**

Étant donnés deux entiers non nuls, affichez "OUI" si l'un des deux est positif (mais pas les deux) et "NON" sinon.

## Exemple d'entrée #1

```
-5
10
```

## Exemple de sortie #1

```
OUI
```

## Exemple d'entrée #2

```
5
10
```

## Exemple de sortie #2

```
NON
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
if a > 0 and b < 0 or a < 0 and b > 0:
  print('OUI')
else:
  print('NON')
```
````
