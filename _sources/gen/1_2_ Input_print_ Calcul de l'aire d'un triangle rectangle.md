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

# 1.2. Input/print: Calcul de l'aire d'un triangle rectangle

## Consigne

Écrire un programme qui lit la longueur de la base et la hauteur d'un triangle rectangle et affiche l'aire. Chaque nombre sera entré séparément.



## Exemple d'entrée

```
3
5
```

## Exemple de sortie

```
7.5
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lecture des nombres b et h comme ci-dessous :
b = int(input())

# Afficher le résultat avec : print()
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
b = int(input())
h = int(input())
print(b * h / 2)
```
````
