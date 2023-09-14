# 9.4. Sets : déjà vu

## Consignes

Étant donnée une série de nombres (séparés par des espaces) entrée au clavier, les analyser de gauche à droite et pour chaque nombre, afficher `YES` si ce nombre a déjà été rencontré dans la série, et `NO` s'il apparaît pour la première fois

## Exemple d'entrée

```
1 2 3 2 3 4
```

## Exemple de sortie

```
NO
NO
NO
YES
YES
NO
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire une chaîne de caractères au clavier :
# s = input()
# Afficher la valeur de s :
# print(s)
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
a = [int(s) for s in input().split()]
seen = set()
for i in a:
  if i in seen:
    print('YES')
  else:
    print('NO')
  seen.add(i)
```
````
