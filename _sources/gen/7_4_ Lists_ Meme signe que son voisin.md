# 7.4. Lists: Même signe que son voisin

## Consigne

À partir d'une liste de nombres entiers différents de 0 donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher la première paire d'élément adjacent qui ont le même signe. S'il n'y a aucune pair, afficher **0**.

## Exemple d'entrée #1

```
-1 2 3 -1 -2
```

## Exemple de sortie #1

```
2 3
```

## Exemple d'entrée #2

```
1 -3 4 -2 1
```

## Exemple de sortie #2

```
0
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read a list of integers:
# a = [int(s) for s in input().split()]
# Print a value:
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
a = [int(s) for s in input().split()]
found = False
for i in range(1, len(a)):
  if a[i - 1] * a[i] > 0:
    print(a[i - 1], a[i])
    found = True
    break
if not found :
  print(0)
```
````
