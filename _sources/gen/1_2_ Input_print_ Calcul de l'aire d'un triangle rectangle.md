# 1.2. Input/print: Calcul de l'aire d'un triangle rectangle

## Consigne

Écrire un programme qui lit la longueur de la base et la hauteur d'un triangle rectangle et affiche l'aire. Chaque nombre sera entré séparément.



## Exemple d'entrée

```
3
5
```

## Exemple de sortie

```
7.5
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
    # Lecture des nombres b et h comme ci-dessous :
b = int(input())
# Afficher le résultat avec : print()
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
b = int(input())
h = int(input())
print(b * h / 2)
```
````
