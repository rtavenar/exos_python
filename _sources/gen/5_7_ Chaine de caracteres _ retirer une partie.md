# 5.7. Chaîne de caractères : retirer une partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, retirer de cette chaîne la première et la dernière occurrence de la lettre `h` ainsi que tous les caractères se trouvant entre ces deux occurrences.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In tobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind


## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
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
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
```
````
