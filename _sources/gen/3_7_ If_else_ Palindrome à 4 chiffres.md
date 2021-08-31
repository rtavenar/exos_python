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

# 3.7. If/else: Palindrome à 4 chiffres

## **Énoncé**

Étant donné un nombre à 4 chiffres, affichez "OUI" si c'est un palindrome (c'est-à-dire qu'on obtient la même valeur en le lisant de droite à gauche ou de gauche à droite) et "NON" sinon.

## Exemple d'entrée #1

```
1221
```

## Exemple de sortie #1

```
OUI
```

## Exemple d'entrée #2

```
1234
```

## Exemple de sortie #2

```
NON
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x = int(input())
milliers = x // 1000
centaines = x // 100 % 10
dizaines = x // 10 % 10
unites = x % 10
if milliers == unites and centaines == dizaines:
  print('OUI')
else:
  print('NON')
```
````
