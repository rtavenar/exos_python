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

# 3.J. If/else: Année bissextile

## **Énoncé**

Étant donné une année, votre programme devra afficher `BISSEXTILE` s'il s'agit d'une année bissextile et  `NORMALE` sinon.

https://fr.wikipedia.org/wiki/Année_bissextile

**Attention.** Les mots `BISSEXTILE` et `NORMALE` devront être écrits en majuscules.

## Exemple d'entrée

```
2012
```

## Exemple de sortie

```
BISSEXTILE
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
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print('BISSEXTILE')
else:
  print('NORMALE')
```
````
