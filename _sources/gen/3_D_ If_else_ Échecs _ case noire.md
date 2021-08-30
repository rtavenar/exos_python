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

# 3.D. If/else: Échecs : case noire

## **Énoncé**

Étant donnés deux entiers indiquant une case de l'échiquier, affichez OUI si c'est une case noire (marron sur le dessin ci-dessous) ou NON sinon.



## **Exemple d'entrée** #1

```
1
1
```

## **Exemple de sortie** #1

```
OUI
```

## **Exemple d'entrée** #2

```
1
2
```

## **Exemple de sortie** #2

```
NON
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#structures-de-contrôle

## Squelette

```{code-cell} python
# Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)
```

````{dropdown} Proposition de solution

```python
x1 = int(input())
y1 = int(input())

if (x1 + y1) % 2 == 0:
  print('OUI')
else:
  print('NON')
```
````
