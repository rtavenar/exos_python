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

# 3.E. If/else: Échecs - même couleur

## **Énoncé**

Étant données deux cases d'un échiquier, afficher `OUI` si elles sont de même couleur et `NON` sinon.



## **Exemple d'entrée**

```
1
1
2
6
```

## **Exemple de sortie**

```
OUI
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
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 + y1) % 2 == (x2 + y2) % 2:
  print('OUI')
else:
  print('NON')
```
````
