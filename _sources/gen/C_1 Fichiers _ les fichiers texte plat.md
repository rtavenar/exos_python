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

# C.1 Fichiers : les fichiers texte plat

**Énoncé**

Codez une fonction `compte_mots` qui prend en entrée un nom de fichier et retourne le nombre de "mots" dans le fichier en question (séparés par des espaces).

**Exemple d'entrée**

```
print(compte_mots("a.txt"))
```

**Exemple de sortie**

```
5
```

**Aide**

https://rtavenar.github.io/poly_python/content/fichiers.html

```{code-cell} bash
:tags: [hide-input, thebe-init]

wget https://raw.githubusercontent.com/rtavenar/exos_python/master/data/C.1%20Fichiers%20%3A%20les%20fichiers%20texte%20plat/a.txt
```

## Squelette

```{code-cell} ipython3

# def compte_mots(nom_du_fichier):
#   # Codez ici votre fonction et modifiez la valeur de retour si besoin
#   return None
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def compte_mots(nom_de_fichier):
  texte = open(nom_de_fichier, "r", encoding="utf-8").read()
  return len(texte.split())
```
````
