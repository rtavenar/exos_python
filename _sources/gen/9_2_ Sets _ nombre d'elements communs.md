# 9.2. Sets : nombre d'éléments communs

## Consignes

Étant données deux séries de nombres (séparés par des espaces) entrées au clavier l'une après l'autre, compter combien de nombres de la première série apparaissent dans la seconde et afficher ce comptage.

## Exemple d'entrée

```
1 3 2
4 3 2
```

## Exemple de sortie

```
2
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
print(len(set(input().split()) & set(input().split())))
```
````
