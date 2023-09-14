# 9.1. Sets : nombre d'éléments distincts

## Consignes

Étant donnée une série d'entiers (séparés par des espaces) entrée au clavier, compter combien de nombres différents elle contient et afficher ce comptage. Ce problème peut être résolu en une seule ligne.

## Exemple d'entrée

```
1 2 3 2 1
```

## Exemple de sortie

```
3
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
print(len(set(input().split())))
```
````
