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

# 1.1. Input/print: Somme de trois nombres

## Consigne

Écrire un programme qui prend 3 nombres et affiche leur somme. Chaque nombre sera entré séparément.

## Exemple d'entrée

```
2
3
6
```

## Exemple de sortie

```
11
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

## Squelette

```{code-cell} ipython3

# Ce programme lit 2 nombres et affiche leur somme :
a = int(input())
b = int(input())
print(a + b)

# Vous pouvez modifier ce programme pour lire et faire la somme de 3 nombres
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```
````
