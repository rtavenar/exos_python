# 3.4. If/else: Nombre à 3 chiffres

## Énoncé

Étant donné un entier, affichez "OUI" s'il est composé de 3 chiffres et "NON" sinon.

## Exemple d'entrée #1

```
179
```

## Exemple de sortie #1

```
OUI
```

## Exemple d'entrée #2

```
1234
```

## Exemple de sortie #2

```
NON
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire un entier :
# a = int(input())
# Afficher une valeur :
# print(a)
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
a = int(input())
if a >= 100 and a < 1000:
  print('OUI')
else:
  print('NON')
```
````
