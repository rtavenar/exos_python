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

# 5.A. Chaînes de caractères : retirer un caractère

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, retirer tous les caractères `@` de cette chaîne.

## Exemple d'entrée

```
Bilbo.Baggins@bagend.hobbiton.shire.me
```

## Exemple de sortie

```
Bilbo.Bagginsbagend.hobbiton.shire.me
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

## Squelette

```{code-cell} ipython3

# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(input().replace('@', ''))
```
````
