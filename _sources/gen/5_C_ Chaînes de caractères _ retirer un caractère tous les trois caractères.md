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

# 5.C. Chaînes de caractères : retirer un caractère tous les trois caractères

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, retirer tous ses caractères dont les indices sont divisibles par 3.

## Exemple d'entrée

```
Python
```

## Exemple de sortie

```
yton
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
t = ''
for i in range(len(s)):
  if i % 3 != 0:
    t += s[i]
print(t)
```
````
