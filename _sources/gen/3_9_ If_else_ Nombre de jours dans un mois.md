# 3.9. If/else: Nombre de jours dans un mois

## **Énoncé**

Étant donné un mois - un entier entre 1et 12, affichez le nombre de jours de ce mois pour l'année 2017.

## Exemple d'entrée #1

```
1
```

(Janvier)

## Exemple de sortie #1

```
31
```

## Exemple d'entrée #2

```
2
```

(Février)

## Exemple de sortie #2

```
28
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
month = int(input())
if month == 2:
  print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
  print(30)
else:
  print(31)
```
````
