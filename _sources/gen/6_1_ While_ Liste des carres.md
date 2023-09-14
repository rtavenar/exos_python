# 6.1. While: Liste des carrés

## Énoncé

Pour un entier N donné, affichez (dans l'ordre) tous les carrés d'entiers positifs inférieurs ou égaux à N.

## Exemple d'entrée

```
50
```

## **Exemple de sortie**

```
1 4 9 16 25 36 49
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read an integer:
# a = int(input())
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
n = int(input())
i = 1
while i ** 2 <= n:
  print(i ** 2, end=' ')
  i += 1
```
````
