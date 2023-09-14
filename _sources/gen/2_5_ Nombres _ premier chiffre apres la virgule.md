# 2.5. Nombres : premier chiffre après la virgule

## Consignes

Etant donné un nombre réel positif, afficher son premier chiffre après la virgule (point décimal).

## Exemple d'entrée

```
1.79
```

## Exemple de sortie

```
7
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
# a = float(input())
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
print(int(float(input()) * 10) % 10)
```
````
