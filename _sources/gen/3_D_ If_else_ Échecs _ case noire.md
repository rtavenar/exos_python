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

# 3.D. If/else: Échecs : case noire

## **Énoncé**

Étant donnés deux entiers indiquant une case de l'échiquier, affichez OUI si c'est une case noire (marron sur le dessin ci-dessous) ou NON sinon.



## **Exemple d'entrée** #1

```
1
1
```

## **Exemple de sortie** #1

```
OUI
```

## **Exemple d'entrée** #2

```
1
2
```

## **Exemple de sortie** #2

```
NON
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x1 = int(input())
y1 = int(input())

if (x1 + y1) % 2 == 0:
  print('OUI')
else:
  print('NON')
```
````
