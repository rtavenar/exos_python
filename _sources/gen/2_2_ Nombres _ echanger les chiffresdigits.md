# 2.2. Nombres : échanger les chiffresdigits

## Consignes

Étant donné un entier à deux chiffres, échanger ses chiffres et afficher le résultat.

## Exemple d'entrée

```
79
```

## Exemple de sortie

```
97
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
print(a % 10 * 10 + a // 10)
```
````
