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

# 3.6. If/else: Chiffres croissants

## **Énoncé**

Étant donné un nombre à 3 chiffres, affichez "OUI" si ses trois chiffres sont dans l'ordre strictement croissant de gauche à droite ou "NON" sinon.

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
197
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
x = int(input())
centaines = x // 100
dizaines = x // 10 % 10
unites = x % 10
if centaines < dizaines and dizaines < unites:
  print('OUI')
else:
  print('NON')
```
````