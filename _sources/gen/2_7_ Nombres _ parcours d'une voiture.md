# 2.7. Nombres : parcours d'une voiture

## Consignes

Une voiture peut parcourir une distance de _N_ kilomètres par jour. Combien de jours faudra-t-il pour parcourir une distance de _M_ kilomètres avec cette voiture ? Le programme reçoit deux nombres tapés au clavier : _N_ et _M_.

## Exemple d'entrée

```
700
750
```

## Exemple de sortie

```
2
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
from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
```
````
