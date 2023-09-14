# 5.9. Chaînes de caractères : remplacer

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins une fois le caractère `1`, remplacer dans cette chaîne tous les nombres `1` par le mot `one`.

## Exemple d'entré

```
1+1=2
```

## Exemple de sortie

```
one+one=2
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

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
print(input().replace('1', 'one'))
```
````
