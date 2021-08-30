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

# 4.3. For: Somme de 10 nombres

## Consigne

10 nombres sont donnés en entrée. Lire chaque nombre et afficher leur somme. Utiliser le moins de variable possible.

## Exemple d'entrée

```
0
1
2
3
4
5
6
7
8
9
```

## Exemple de sortie

```
45
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Squelette

```{code-cell} python
# Read an integer:
# a = int(input())
# Print a value:
# print(a)
```

````{dropdown} Proposition de solution

```python
result = 0
for i in range(10):
  result += int(input())
print(result)
```
````
