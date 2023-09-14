# 3.J. If/else: Année bissextile

## **Énoncé**

Étant donné une année, votre programme devra afficher `BISSEXTILE` s'il s'agit d'une année bissextile et  `NORMALE` sinon.

https://fr.wikipedia.org/wiki/Année_bissextile

**Attention.** Les mots `BISSEXTILE` et `NORMALE` devront être écrits en majuscules.

## Exemple d'entrée

```
2012
```

## Exemple de sortie

```
BISSEXTILE
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire un entier :
# a = int(input())
# Afficher une valeur :
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
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print('BISSEXTILE')
else:
  print('NORMALE')
```
````
