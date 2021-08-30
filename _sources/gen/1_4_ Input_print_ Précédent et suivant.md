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

# 1.4. Input/print: Précédent et suivant

## Consigne

Écrire un programme qui lit un nombre entier et affiche le nombre précédent et le nombre suivant (Cf. exemple ci-dessous).

## Exemple d'entrée

```
179
```

## Exemple de sortie

```
Le nombre suivant 179 est 180
Le nombre précédant 179 est 178
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

## Squelette

```{code-cell} python
# Lire un entier :
# a = int(input())
# Afficher la valeur de a :
# print(a)
```

````{dropdown} Proposition de solution

```python
n = int(input())
print('Le nombre suivant ' + str(n) + ' est ' + str(n + 1))
print('Le nombre précédant ' + str(n) + ' est ' + str(n - 1))
```
````
