# 3.1. If/else: Pair ou impair

## Consigne

Étant donné un entier, afficher "pair" s'il est pair ou "impair" sinon.

## Exemple d'entrée #1

```
5
```

## Exemple de sortie #1

```
impair
```

## Exemple d'entrée #2

```
6
```

## Exemple de sortie #2

```
pair
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire un entier
# a = int(input())
# Afficher une valeur:
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
if int(input()) % 2 == 0:
  print('pair')
else:
  print('impair')
```
````
