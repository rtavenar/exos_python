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

# 9.5. Sets : deviner le nombre

## Consignes

Auguste et Béatrice jouent au jeu suivant. Auguste choisi dans sa tête un nombre secret entier entre 1 et `n`. Béatrice essaie de deviner le nombre secret en fournissant un ensemble d'entiers. Auguste répond `YES` si son nombre secret existe dans l'ensemble fourni, ou `NO`, dans le cas contraire. Après quelques questions Béatrice, complètement perdue, vous demande de l'aider à trouver le nombre secret d'Auguste.

On entrera au début du programme le nombre entier positif `n` déterminant la limite haute du nombre secret. Ensuite le jeu commence et tourne en boucle : on donnera les essais de Béatrice entrés au clavier sous forme à chaque fois d'une série de nombres entiers séparés par des espaces, suivis de la réponse d'Auguste (`YES` ou `NO`) entrée elle aussi au clavier. Cette boucle continue jusqu'à ce que Béatrice demande de l'aide en entrant `HELP` au clavier, à la place de sa série de nombres. Quand Béatrice demande cette aide, afficher une liste de toutes les possibilités restantes pour le nombre secret, par ordre croissant, séparées par un espace.

## Exemple d'entrée

```
10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP
```

## Exemple de sortie

```
1 3 5
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

## Squelette

```{code-cell} python
# Lire une chaîne de caractères au clavier :
# s = input()
# Afficher la valeur de s :
# print(s)
```

````{dropdown} Proposition de solution

```python
n = int(input())
possible = set(range(n))
while True:
  line = input()
  if line == 'HELP':
    break
  guess = set([int(s) for s in line.split()])
  if input() == 'YES':
    possible &= guess
  else:
    possible -= guess
print(*sorted(possible))
```
````
