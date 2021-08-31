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

# 5.9. Chaînes de caractères : remplacer

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins une fois le caractère `1`, remplacer dans cette chaîne tous les nombres `1` par le mot `one`.

## Exemple d'entré

```
1+1=2
```

## Exemple de sortie

```
one+one=2
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

## Squelette

```{code-cell} ipython3

# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(input().replace('1', 'one'))
```
````
