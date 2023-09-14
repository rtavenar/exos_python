# 5.A. Chaînes de caractères : retirer un caractère

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, retirer tous les caractères `@` de cette chaîne.

## Exemple d'entrée

```
Bilbo.Baggins@bagend.hobbiton.shire.me
```

## Exemple de sortie

```
Bilbo.Bagginsbagend.hobbiton.shire.me
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
print(input().replace('@', ''))
```
````
