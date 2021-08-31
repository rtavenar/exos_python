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

# 5.4. Chaînes de caractères : échanger deux mots

## Consignes

Étant donnée une chaîne de caractères entrée au clavier formée exactement de deux mots séparés par un espace, afficher une nouvelle chaîne avec le premier et le second mot échangés et séparés par un espace : le second mot est affiché en premier. On considérera comme un mot toute série de caractères adjacents différents d'un espace.


Peut-on résoudre le problème sans utiliser `if-else` et une boucle?

## Exemple d'entrée

```
Hello, world!
```

## Exemple de sortie

```
world! Hello,
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#str.split

## Squelette

```{code-cell} python
:tags: [remove-stderr]

# Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
word1, word2 = input().split()
print(word2, word1)
```
````
