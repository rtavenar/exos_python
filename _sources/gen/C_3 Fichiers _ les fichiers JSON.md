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

## Squelette

```{code-cell} ipython3

# import json
# 
# def compte_cles_prefixe(nom_du_fichier, prefixe):
#   # Codez votre fonction ici et modifiez sa valeur de retour si besoin
#   return None
# 
```

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
