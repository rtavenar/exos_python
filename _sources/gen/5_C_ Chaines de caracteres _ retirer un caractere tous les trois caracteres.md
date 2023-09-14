# 5.C. Chaînes de caractères : retirer un caractère tous les trois caractères

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, retirer tous ses caractères dont les indices sont divisibles par 3.

## Exemple d'entrée

```
Python
```

## Exemple de sortie

```
yton
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

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
t = ''
for i in range(len(s)):
  if i % 3 != 0:
    t += s[i]
print(t)
```
````
