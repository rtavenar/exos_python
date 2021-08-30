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

# 5.3. Chaînes de caractères : deux moitiés

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, la découper en deux parties égales. Si la longueur est impaire, garder le caractère du milieu dans le premier découpage de sorte que la première chaîne découpée contienne un caractère de plus que la seconde. Ensuite, afficher une nouvelle chaîne de caractères sur une seule ligne avec les deux parties découpées échangées : la seconde moitié en premier et la première moitié en dernier.

Peut-on résoudre le problème sans utiliser `if`?

## Exemple d'entrée

```
Qwerty
```

## Exemple de sortie

```
rtyQwe
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

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
mid = (len(s) + 1) // 2
print(s[mid:] + s[:mid])
```
````
