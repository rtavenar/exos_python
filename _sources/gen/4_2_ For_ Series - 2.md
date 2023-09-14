# 4.2. For: Series - 2

## Consigne

Soit deux entiers A et B donnés en entrée. Afficher tous les nombres de A à B bornes comprises, par ordre croissant, si A < B ou par ordre décroissant si A ≥ B.

## Exemple d'entrée

```
8
5
```

## Exemple de sortie

```
8 7 6 5
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

if a < b:
  for i in range(a, b + 1):
    print(i, end=' ')
else:
  for i in range(a, b - 1, -1):
    print(i, end=' ')
```
````
