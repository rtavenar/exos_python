# 1.5. Input/print: Partage de pommes

## Consigne

`N étudiants prennent K pommes et les distribuent de façon homogène entre les étudiants. Le reste (la partie indivisible) des pommes reste dans le panier. Combien de pommes a obtenu chaque étudiant ? Combien de pommes reste-t-il dans le panier ?`

Le programme lit les nombres N et K et devra afficher la réponse aux deux questions ci-dessus.


## Exemple d'entrée

```
6
50
```

## Exemple de sortie

```
8
2
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read the numbers like this:
# n = int(input())
# Print the result with print()
# Example of division, integer division and remainder:
print(63 / 5)
print(63 // 5)
print(63 % 5)
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
k = int(input())
print(k // n)
print(k % n)
```
````
