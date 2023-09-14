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

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    import csv

def nb_non_vides(nom_du_fichier):
  # Codez votre fonction ici et modifiez la valeur de retour si besoin
  return None
</py-repl>
<py-terminal id="my-terminal"></py-terminal>
<py-script>
from js import document as _DOC
def clear_term():
    ter = _DOC.getElementById("my-terminal").firstChild
    ter.innerHTML = ''
</py-script>
<button py-click="clear_term()" id="clear-terminal" class="py-button">Nettoyer la console de sortie</button>


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
