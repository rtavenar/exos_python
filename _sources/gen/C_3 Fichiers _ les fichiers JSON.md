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

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': 'import json\n\ndef compte_cles_prefixe(nom_du_fichier, prefixe):\n  # Codez votre fonction ici et modifiez sa valeur de retour si besoin\n  return None\n', 'files': {'a.json': {'type': 'text', 'body': '{\n  "abd": 12,\n  "abcdef": 1,\n  "cv": {\n    "abcd": 3\n  },\n  "abc": 2\n}'}, 'b.json': {'type': 'text', 'body': '{\n  "abcd": 12,\n  "abcdef": 1,\n  "cv": {\n    "abcd": 3\n  },\n  "abc": 2\n}'}}})</script>


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
