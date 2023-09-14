# 4.4. For: Somme de N nombres

## Consigne

N nombres sont donnés en entrés. Lire chaque nombre et afficher la leur somme.

Le premier nombre entré est un entier N, qui est le nombre d'entiers qui seront entrés. Chacune des N entrées contient un entier. Afficher la somme de ces N entiers.


## Exemple d'entrée

```
10
1
2
1
1
1
1
3
1
1
1
```

## Exemple de sortie

```
13
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
  result += int(input())
print(result)
```
````
