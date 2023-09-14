# 2.D. Nombres : bureaux d'une école

## Consignes

Une école a décidé de remplacer les bureaux dans trois classes. Chaque bureau peut accueillir deux élèves. Étant donné le nombre d'élèves pour chaque classe, afficher le plus petit nombre de bureaux pouvant être achetés.

Le programme doit lire trois entiers : le nombre d'élèves dans chacune des trois classes, `a`, `b` et `c` respectivement.

Dans l'exemple ci-dessous il y a trois classes. La première classe contient 20 élèves et a donc besoin de 10 bureaux. La deuxième classe contient 21 élèves qui vont donc avoir besoin de 11 bureaux. 11 bureaux sont suffisants également pour la troisième classe qui compte 22 élèves. Au total, nous avons donc besoin de 32 bureaux.


## Exemple d'entrées

```
20
21
22
```

## Exemple de sortie

```
32
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire un entier :
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
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)
```
````