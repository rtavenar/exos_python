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

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    def compte_mots(nom_du_fichier):
  # Codez ici votre fonction et modifiez la valeur de retour si besoin
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
def compte_mots(nom_de_fichier):
  texte = open(nom_de_fichier, "r", encoding="utf-8").read()
  return len(texte.split())
```
````
