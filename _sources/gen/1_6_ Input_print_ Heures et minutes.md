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

# 1.6. Input/print: Heures et minutes

## Consigne

Soit un entier N, représentant le nombre de secondes écoulées depuis minuit, calculer le nombre d'heures entières et le nombre de minutes entières écoulées depuis minuit.


Le programme devra afficher les deux nombres : le nombre d'heures (entre 0 et 23) et le nombre de minute (entre 0 et 1339).


Par exemple, si N = 3900, alors 3900 secondes se sont écoulées depuis minuit (il est donc 1h05). Le programme devra afficher **1 65** ( 1 heure entière depuis minuit, 65 minutes entières depuis minuit).

## Exemple d'entrée

```
3900
```

## Exemple de sortie

```
1 65
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

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
num_seconds = int(input())
print(num_seconds // 3600, num_seconds // 60)
```
````
