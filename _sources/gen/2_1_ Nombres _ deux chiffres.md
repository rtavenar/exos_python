# 2.1. Nombres : deux chiffres

## Consignes

Étant donné un entier à deux chiffres, afficher son premier chiffre (dizaines) puis son deuxième chiffre (unités). Utiliser l'opérateur de division entière pour obtenir le chiffre des dizaines et l'opérateur de modulo (reste de la division entière) pour obtenir le chiffre des unités.

## Exemple d'entrée

```
79
```

## Exemple de sortie

```
7 9
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
print(a // 10, a % 10)
```
````
