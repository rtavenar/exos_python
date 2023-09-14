# 6.E. While: plus grande sous-série

## Consignes

Étant données une série d'entiers non négatifs entrés au clavier un par un (un entier par ligne) et se terminant par `0`,  déterminer et afficher la longueur de la plus grande sous-série de nombres identiques à l'intérieur de la série saisie.

## Exemple d'entrée

```
1
**7**
**7**
**7**
9
1
1
0
```

(les nombres appartenant à la sous-série maximale sont soulignés)

## Exemple de sortie

```
3
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
next = int(input())
length = 1
max_length = 1
while next != 0:
  prev, next = next, int(input())
  if prev == next:
    length += 1
  else:
    length = 1
  max_length = max(length, max_length)
print(max_length)
```
````
