# 5.5. Chaînes de caractères : première et dernière occurences

## Consignes

Étant donnée une chaîne de caractères entrée au clavier qui peut contenir la lettre `f`, afficher l'indice des première et dernière occurrences de `f` dans cette chaîne. Si la lettre `f` n'apparait qu'une seule fois, afficher son indice une seule fois. Si la lettre `f` n'apparait pas dans la chaîne, afficher `-1`.

## Exemple d'entrée #1

```
comfort
```

## Exemple de sortie #1

```
3
```

## Exemple d'entrée #2

```
office
```

##  Exemple de sortie #2

```
1 2
```

##  Exemple d'entrée #3

```
hello
```

## Exemple de sortie #3

```
-1
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

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
if s.find('f') == s.rfind('f'):
  print(s.find('f'))
else:
  print(s.find('f'), s.rfind('f'))
```
````
