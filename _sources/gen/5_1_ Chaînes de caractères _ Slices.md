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

# 5.1. Chaînes de caractères : Slices

## Consignes

Étant donnée une chaîne de caractères entrée au clavier :

1. Sur la première ligne, afficher le troisième caractère de cette chaîne.
2. Sur la seconde ligne, afficher du deuxième jusqu'au dernier caractère de cette chaîne.
3. Sur la troisième ligne, afficher les cinq premiers caractères de la chaîne.
4. Sur la quatrième, afficher tous les caractères sauf les deux derniers de la chaîne.
5. Sur la cinquième ligne, afficher tous les caractères d'indices pairs (attention, se rappeler que les indices commencent à 0, donc les caractères sont affichés en commençant par le premier).
6. Sur la sixième ligne, afficher les caractères de la chaîne, tous les deux caractères et en commençant par le second caractère de la chaîne.
7. Sur la septième ligne afficher tous les caractères de la chaîne en sens inverse.
8. Sur la huitième ligne, afficher la chaîne à l'envers, tous les deux caractères, en commençant par le dernier.
9. Sur la neuvième ligne, afficher la longueur de la chaîne saisie.

## Exemple d'entrée

```
Abrakadabra
```

## Exemple de sortie

```
r
brakadabra
Abrak
Abrakadab
Arkdba
baaar
arbadakarbA
abdkrA
11
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

## Squelette

```{code-cell} python
# Lire une chaîne de caractères :
# s = input()
# Afficher la chaîne s :
# print(s)
```

````{dropdown} Proposition de solution

```python
s = input()
print(s[2])
print(s[1:])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))
```
````
