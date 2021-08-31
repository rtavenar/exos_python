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

# 6.3. While: Puissances de 2

## **Énoncé**

Étant donné un entier X, on cherche le plus grand entier **n** pour lequel **2ⁿ** est inférieur ou égal à X. Affichez **n** et **2ⁿ**.


## **Exemple d'entrée**

```
50
```

## **Exemple de sortie**

```
5 32
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

## Squelette

```{code-cell} ipython3

# Read an integer:
# a = int(input())
# Print a value:
# print(a)

```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x = int(input())
n = 1
while 2 ** n <= x:
  n += 1
print(n - 1, 2 ** (n - 1))
```
````
