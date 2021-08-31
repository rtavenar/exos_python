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

# 2.8. Nombres : siècle

## Consigne

Étant donnée une année (entrée au clavier comme un entier positif) trouver et afficher le siècle correspondant. Noter que, par exemple, le 20ème siècle commence avec l'année 1901.

## Example input

```
2000
```

## Example output

```
20
```

## Theory

If you don't know how to start solving this assignment, please, review a theory for this lesson:

https://snakify.org/lessons/integer_float_numbers/


You may also try step-by-step theory chunks:

https://snakify.org/lessons/integer_float_numbers/steps/1/

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
a = int(input())
print((a - 1) // 100 + 1)
```
````
