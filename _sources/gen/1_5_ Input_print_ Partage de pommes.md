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

# 1.5. Input/print: Partage de pommes

## Consigne

`N étudiants prennent K pommes et les distribuent de façon homogène entre les étudiants. Le reste (la partie indivisible) des pommes reste dans le panier. Combien de pommes a obtenu chaque étudiant ? Combien de pommes reste-t-il dans le panier ?`

Le programme lit les nombres N et K et devra afficher la réponse aux deux questions ci-dessus.


## Exemple d'entrée

```
6
50
```

## Exemple de sortie

```
8
2
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

## Squelette

```{code-cell} ipython3

# Read the numbers like this:
# n = int(input())

# Print the result with print()

# Example of division, integer division and remainder:
print(63 / 5)
print(63 // 5)
print(63 % 5)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
n = int(input())
k = int(input())
print(k // n)
print(k % n)
```
````