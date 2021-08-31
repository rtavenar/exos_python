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

# 3.3. If/else: Signe

## Énoncé

Étant donné un entier, afficher `1` s'il est positif, `-1` s'il est négatif, ou `0` s'il est nul.

Essayez d'utiliser la syntaxe `if-elif-else` pour cela.

## Exemple d'entrée

```
179
```

## Exemple de sortie

```
1
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Squelette

```{code-cell} ipython3

# Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x = int(input())
if x > 0:
  print(1)
elif x < 0:
  print(-1)
else:
  print(0)
```
````
