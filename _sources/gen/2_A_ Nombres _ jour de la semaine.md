# 2.A. Nombres : jour de la semaine

## Consignes

Les jours de la semaine sont numérotés de la manière suivantes : 0 —Dimanche, 1 — Lundi, 2 — Mardi, ..., 6 — Samedi. Le programme reçoit un entier _K_ compris entre 1 et 365. Trouver et afficher le numéro du jour de la semaine du _K_-ième jour de l'année sachant que le 1er janvier de cette année est un jeudi.


## Exemple d'entrée

```
1
```

## Exemple de sortie

```
4
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
print((int(input()) + 3) % 7)
```
````
