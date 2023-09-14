# 3.6. If/else: Chiffres croissants

## **Énoncé**

Étant donné un nombre à 3 chiffres, affichez "OUI" si ses trois chiffres sont dans l'ordre strictement croissant de gauche à droite ou "NON" sinon.

## Exemple d'entrée #1

```
179
```

## Exemple de sortie #1

```
OUI
```

## Exemple d'entrée #2

```
197
```

## Exemple de sortie #2

```
NON
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
x = int(input())
centaines = x // 100
dizaines = x // 10 % 10
unites = x % 10
if centaines < dizaines and dizaines < unites:
  print('OUI')
else:
  print('NON')
```
````
