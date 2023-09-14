# 4.7. For: Nombre de zéros

## Consigne

Soit N nombres : le premier nombre donné en entrée est N, après cela N entiers sont entrés. Compter le nombre de zéros parmi les entiers donnés et afficher le résultat.

Vous devez compter le nombre d'entiers égaux à zéro, mais pas le nombre de zéro qui compose un entier.


## Exemple d'entrée

```
5
0
700
0
200
2
```

## Exemple de sortie

```
2
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
result = 0
for i in range(int(input())):
  if int(input()) == 0:
    result += 1
print(result)
```
````
