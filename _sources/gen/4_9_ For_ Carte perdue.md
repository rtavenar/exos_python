# 4.9. For: Carte perdue

## Consigne

Soit un ensemble de cartes portant les numéros de 1 à N. L'une des cartes a été perdue. Déterminer le numéro de la carte perdue à partie des numéros des cartes restantes.

Entrer un nombre N, suivi par N-1 entiers représentant les numéros des cartes restantes (valeurs distinctes d'entiers dans l'interval 1 à N). Trouver et afficher le numéro de la carte manquante.


## Exemple d'entrée

```
5
3
5
2
1
```

## Exemple de sortie

```
4
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read an integer:
# a = int(input())
# Print a value:
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
n = int(input())

cards_sum = 0
for i in range(1, n + 1):
  cards_sum += i

for i in range(n - 1):
  cards_sum -= int(input())

print(cards_sum)
```
````
