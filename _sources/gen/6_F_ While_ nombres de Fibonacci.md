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

# 6.F. While: nombres de Fibonacci

## Consignes



Les nombres de Fibonacci sont les nombres de la suite d'entiers commençant par `1,1` et où chaque nombre après ces deux premiers est la somme des deux précédents :

`1,1,2,3,5,8,13,21,34,...`

Étant donné un entier strictement positif `n` entré au clavier, calculer et afficher le `n`ième nombre de la suite de Fibonacci.

## Exemple d'entrée

```
6
```

## Exemple de sortie

```
8
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
prev, next = 1, 1
n = int(input())
for i in range(n - 2):
  prev, next = next, prev + next
print(next)
```
````
