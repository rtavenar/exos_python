# 6.G. While: indice de Fibonacci

## Consignes

Les nombres de Fibonacci sont les nombres de la suite d'entiers commençant par `1,1` et où chaque nombre après ces deux premiers est la somme des deux précédents :

`1,1,2,3,5,8,13,21,34,...`


Étant donné un entier plus grand que 1 entré au clavier, déterminer s'il s'agit d'un nombre de la suite de Fibonacci et si c'est le cas, afficher son rang `n` dans cette série (le premier nombre est de rang `1`), sinon afficher `-1`.

## Exemple d'entrée

```
8
```

## Exemple de sortie

```
6
```

## Aide

https://docs.python.org/fr/3.6/reference/compound_stmts.html#the-while-statement

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire un entier au clavier :
# a = int(input())
# Afficher la valeur de a :
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
prev, next = 1, 1
index = 2
possible_fib = int(input())
while possible_fib > next:
  prev, next = next, prev + next
  index += 1
if possible_fib == next:
  print(index)
else:
  print(-1)
```
````
