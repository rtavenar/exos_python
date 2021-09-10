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

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': 'def compte_mots(nom_du_fichier):\n  # Codez ici votre fonction et modifiez la valeur de retour si besoin\n  return None', 'files': {'a.txt': {'type': 'text', 'body': 'Ce fichier contient cinq mots'}, 'b.txt': {'type': 'text', 'body': 'Celui-ci en contient quatre'}}})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def compte_mots(nom_de_fichier):
  texte = open(nom_de_fichier, "r", encoding="utf-8").read()
  return len(texte.split())
```
````
