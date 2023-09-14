# 5.B. Chaîne de caractères : remplacer dans une sous-partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, remplacer toutes les occurrences de `h` par `H`, sauf la première et la dernière.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In the Hole in tHe ground tHere lived a hobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire une chaîne de caractères au clavier :
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
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle.replace('h', 'H') + right)
```
````
