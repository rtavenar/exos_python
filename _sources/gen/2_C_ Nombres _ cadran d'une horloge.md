# 2.C. Nombres : cadran d'une horloge

## Consignes

L'aiguille des heures d'une horloge analogique a tourné de α degrés depuis minuit. Déterminer de combien de degrés l'aiguille des minutes a tourné depuis l'heure en cours. Les entrées et sorties de ce programme sont des entiers.

## Exemple d'entrée (angle en degrés de l'aiguille des heures)

```
190
```

(6h20)

## Exemple de sortie (angle en degrés de l'aiguille des minutes)

```
120
```

(20 min)

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
print(int(input()) % 30 * 12)
```
````
