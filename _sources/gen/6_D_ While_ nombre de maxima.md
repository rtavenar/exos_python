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

# 6.D. While: nombre de maxima

## Consignes

Étant donnée une série d'entiers non-négatifs entrés un à un au clavier (un entier par ligne) et se terminant par `0`, trouver combien d'éléments de cette série sont égaux à son élément le plus grand et afficher ce nombre.

## Exemple d'entrées #1

```
1
7
9
0
```

## Exemple de sortie #1

```
1
```

## Exemple d'entrées #2

```
1
3
3
1
0
```

## Exemple de sortie #2

```
2
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
maximum = int(input())
counter = 1
a = -1
while a != 0:
  a = int(input())
  if a > maximum:
    maximum, counter = a, 1
  elif a == maximum:
    counter += 1
print(counter)
```
````