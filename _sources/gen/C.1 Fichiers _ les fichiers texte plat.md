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

http://rtavenar.github.io/teaching/python_poly/html/poly.html#lecture-de-fichiers-textuels

## Squelette

```python
def compte_mots(nom_du_fichier):
  # Codez ici votre fonction et modifiez la valeur de retour si besoin
  return None
```

## Proposition de solution

```python
def compte_mots(nom_de_fichier):
  texte = open(nom_de_fichier, "r", encoding="utf-8").read()
  return len(texte.split())
```

