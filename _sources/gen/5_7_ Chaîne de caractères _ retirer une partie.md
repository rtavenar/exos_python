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

# 5.7. Chaîne de caractères : retirer une partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, retirer de cette chaîne la première et la dernière occurrence de la lettre `h` ainsi que tous les caractères se trouvant entre ces deux occurrences.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In tobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind


## Squelette

```{code-cell} python
# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
```

````{dropdown} Proposition de solution

```python
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
```
````
