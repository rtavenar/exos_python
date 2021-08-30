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

# B.2 Fonctions : passage d'un paramètre

**Énoncé**

Codez une fonction affichage_bienvenue qui affiche le message "Bienvenue XXX" et ajoute le prénom d'une personne ('XXX'). La fonction prend en paramètre le prénom de la personne.

**Exemple d'appel de la fonction**

```
affichage_bienvenue('Régis')
```

**Exemple de sortie**

```
Bienvenue Régis
```

**Aide**

http://rtavenar.github.io/teaching/python_poly/html/poly.html#fonctions

## Squelette

```{code-cell} python
def affichage_bienvenue():
  # Codez votre fonction ici (et affichez le message de bienvenue !)
```

````{dropdown} Proposition de solution

```python
def affichage_bienvenue(prenom):
  # Codez votre fonction ici (et affichez le message de bienvenue !)
  print('Bienvenue '+ prenom)
```
````
