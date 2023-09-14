# 4.1. For: Series - 1

## Consigne

Soit deux entiers A et B (A ≤ B) donnés en entrée. Afficher tous les nombres de A à B bornes comprises.

## Exemple d'entrée

```
1
10
```

## Exemple de sortie

```
1 2 3 4 5 6 7 8 9 10
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

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
a = int(input())
b = int(input())

for i in range(a, b + 1):
  print(i, end=' ')
```
````
