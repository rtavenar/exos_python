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

# 5.2. Chaînes de caratères : nombre de mots

## Consignes

Étant donnée une chaîne de caractères (entrée au clavier) représentant des mots séparés par des espaces, déterminer le nombre de mots la composant. Pour résoudre le problème, utiliser la méthode `split` des chaînes de caractères.

## Exemple d'entrée

```
Hello world
```

## Exemple de sortie

```
2
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#str.split

## Squelette

```{code-cell} ipython3

# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(len(input().split()))
```
````
