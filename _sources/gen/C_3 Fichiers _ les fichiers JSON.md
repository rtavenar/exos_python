# C.3 Fichiers : les fichiers JSON

**Énoncé**

Codez une fonction qui lit un fichier JSON et, pour un préfixe passé en argument, retourne le nombre de clés de premier niveau du fichier JSON qui commencent par le préfixe.

**Exemple d'entrée**

```
print(compte_cles_prefixe("a.json", "abc"))
```

**Exemple de sortie**

```
2
```

**Aide**

https://rtavenar.github.io/poly_python/content/fichiers.html

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    import json

def compte_cles_prefixe(nom_du_fichier, prefixe):
  # Codez votre fonction ici et modifiez sa valeur de retour si besoin
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
import json

def compte_cles_prefixe(nom_du_fichier, prefixe):
  d = json.load(open(nom_du_fichier, "r", encoding="utf-8"))
  n = 0
  for k in d.keys():
    if k.startswith(prefixe):
      n += 1
  return n
```
````
