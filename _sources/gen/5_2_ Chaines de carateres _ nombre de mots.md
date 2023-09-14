# 5.2. Chaînes de caratères : nombre de mots

## Consignes

Étant donnée une chaîne de caractères (entrée au clavier) représentant des mots séparés par des espaces, déterminer le nombre de mots la composant. Pour résoudre le problème, utiliser la méthode `split` des chaînes de caractères.

## Exemple d'entrée

```
Hello world
```

## Exemple de sortie

```
2
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#str.split

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
print(len(input().split()))
```
````
