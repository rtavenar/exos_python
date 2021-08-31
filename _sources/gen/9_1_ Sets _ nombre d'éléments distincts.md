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

# 9.1. Sets : nombre d'éléments distincts

## Consignes

Étant donnée une série d'entiers (séparés par des espaces) entrée au clavier, compter combien de nombres différents elle contient et afficher ce comptage. Ce problème peut être résolu en une seule ligne.

## Exemple d'entrée

```
1 2 3 2 1
```

## Exemple de sortie

```
3
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lire une chaîne de caractères au clavier :
# s = input()
# Afficher la valeur de s :
# print(s)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(len(set(input().split())))
```
````
