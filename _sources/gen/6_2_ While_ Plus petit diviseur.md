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

# 6.2. While: Plus petit diviseur

## **Énoncé**

Étant donné un entier strictement plus grand que 1, afficher son plus petit diviseur strictement supérieur à 1.

## **Exemple d'entrée**

```
15
```

## **Exemple de sortie**

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

## Squelette

```{code-cell} ipython3

# Read an integer:
# a = int(input())
# Print a value:
# print(a)
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
i = 2
while a % i != 0:
  i += 1
print(i)
```
````
