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

# 6.E. While: plus grande sous-série

## Consignes

Étant données une série d'entiers non négatifs entrés au clavier un par un (un entier par ligne) et se terminant par `0`,  déterminer et afficher la longueur de la plus grande sous-série de nombres identiques à l'intérieur de la série saisie.

## Exemple d'entrée

```
1
**7**
**7**
**7**
9
1
1
0
```

(les nombres appartenant à la sous-série maximale sont soulignés)

## Exemple de sortie

```
3
```

## Aide

https://docs.python.org/fr/3.6/reference/compound_stmts.html#the-while-statement

## Squelette

```{code-cell} ipython3

# Lire un entier au clavier :
# a = int(input())
# Afficher la valeur de a :
# print(a)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
next = int(input())
length = 1
max_length = 1
while next != 0:
  prev, next = next, int(input())
  if prev == next:
    length += 1
  else:
    length = 1
  max_length = max(length, max_length)
print(max_length)
```
````
