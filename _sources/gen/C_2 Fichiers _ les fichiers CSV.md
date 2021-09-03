# C.2 Fichiers : les fichiers CSV

**Énoncé**

Codez une fonction qui compte le nombre de cellules non vides d'un fichier CSV séparé par des points-virgules.

**Exemple d'entrée**

```
print(nb_non_vides("a.csv"))
```

**Exemple de sortie**

```
8
```

**Aide**

https://rtavenar.github.io/poly_python/content/fichiers.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': 'import csv\n\ndef nb_non_vides(nom_du_fichier):\n  # Codez votre fonction ici et modifiez la valeur de retour si besoin\n  return None\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
import csv

def nb_non_vides(nom_de_fichier):
  reader = csv.reader(open(nom_de_fichier, "r", encoding="utf-8"), delimiter=";")
  n = 0
  for ligne in reader:
    for cellule in ligne:
      if cellule.strip() != "":
        n += 1
  return n
```
````
