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

# 3.4. If/else: Nombre à 3 chiffres

## Énoncé

Étant donné un entier, affichez "OUI" s'il est composé de 3 chiffres et "NON" sinon.

## Exemple d'entrée #1

```
179
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
a = int(input())
if a >= 100 and a < 1000:
  print('OUI')
else:
  print('NON')
```
````
