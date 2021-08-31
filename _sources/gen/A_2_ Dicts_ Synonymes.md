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

# A.2. Dicts: Synonymes

## Consigne

Soit un dictionnaire composé de paires de mots. Chaque mot est un synonyme de l'autre mot dans sa paire.

À partir d'une liste de paires de mots, vous devrez créer un tel dictionnaire.

À la suite du dictionnaire, l'utilisateur propose un mot en entrée pour obtenir le synonyme. La réponse sera la valeur correspondant à la clé (mot proposé en entrée).


## Exemple d'entrée

```
3
Hello Hi
Bye Goodbye
List Array
Goodbye
```

## Exemple de sortie

```
Bye
```

## Aide

https://rtavenar.github.io/poly_python/content/dict.html

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Read a string:
# s = input()
# Print a value:
# print(s)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
synonyms = {}
for i in range(int(input())):
  w1, w2 = input().split()
  synonyms[w1] = w2
  synonyms[w2] = w1
print(synonyms[input()])
```
````
