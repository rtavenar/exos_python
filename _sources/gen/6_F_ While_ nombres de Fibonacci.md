# 6.F. While: nombres de Fibonacci

## Consignes



Les nombres de Fibonacci sont les nombres de la suite d'entiers commençant par `1,1` et où chaque nombre après ces deux premiers est la somme des deux précédents :

`1,1,2,3,5,8,13,21,34,...`

Étant donné un entier strictement positif `n` entré au clavier, calculer et afficher le `n`ième nombre de la suite de Fibonacci.

## Exemple d'entrée

```
6
```

## Exemple de sortie

```
8
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
n = int(input())
for i in range(n - 2):
  prev, next = next, prev + next
print(next)
```
````
