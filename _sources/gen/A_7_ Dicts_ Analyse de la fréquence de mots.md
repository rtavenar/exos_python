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

# A.7. Dicts: Analyse de la fréquence de mots

## Consigne

Sois un nombre **n**, suivi par **n** lignes de texte.

Affichez tous les mots présents dans le texte entré (un mot par ligne) en indiquant le nombre d'occurrences de chacun des mots. Les mots devront être classés par ordre d'occurrences décroissantes puis par ordre alphabétique en cas d'égalité d'occurrence.

**Indication :** Après avoir créé un dictionnaire des mots et de leurs fréquences, on souhaite le trier en fonction des fréquences. Cela  peut être réalisé en créant une liste dont les éléments sont des  listes de deux éléments : le nombre d'occurrences d'un mot et le mot  lui-même. Par exemple, [[2, 'hi'], [1, 'what'], [3, 'is']]. Le tri de liste standard permet de trier une liste de listes, selon le premier élément, puis selon le deuxième  élément.

## Exemple d'entrée

```
9
hi
hi
what is your name
my name is bond
james bond
my name is damme
van damme
claude van damme
jean claude van damme
```

## Exemple de sortie

```
damme 4
is 3
name 3
van 3
bond 2
claude 2
hi 2
my 2
james 1
jean 1
what 1
your 1
```

## Aide

https://rtavenar.github.io/poly_python/content/dict.html

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

## Squelette

```{code-cell} ipython3

# Read a string:
# s = input()
# Print a value:
# print(s)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
frequency = {}
for _ in range(int(input())):
  for word in input().split():
    if word not in frequency:
      frequency[word] = 0
    frequency[word] += 1
for i in sorted(set(frequency.values()), reverse=True):
  for word in sorted([word for word in frequency if frequency[word] == i]):
    print(word, i)
```
````
