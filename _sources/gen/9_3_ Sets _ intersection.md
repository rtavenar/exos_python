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

# 9.3. Sets : intersection

## Consignes

Étant données deux séries de nombres (séparés par des espaces) entrées l'une après l'autre au clavier, trouver tous les nombres qui apparaissent à la fois dans la première et dans la deuxième séries et les afficher par ordre croissant.

## Exemple d'entrée

```
1 3 2
4 3 2
```

## Exemple de sortie

```
2 3
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

## Squelette

```{code-cell} ipython3

# Lire une chaîne de caractères au clavier :
# s = input()
# Afficher la valeur de s :
# print(s)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
first = set([int(s) for s in input().split()])
second = set([int(s) for s in input().split()])
print(*sorted(first & second))
```
````
