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

# 5.B. Chaîne de caractères : remplacer dans une sous-partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, remplacer toutes les occurrences de `h` par `H`, sauf la première et la dernière.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In the Hole in tHe ground tHere lived a hobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

## Squelette

```{code-cell} ipython3

# Lire une chaîne de caractères au clavier :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle.replace('h', 'H') + right)
```
````
