# 6.4. While: Course à pied

## **Énoncé**

Vous êtes un athlète qui se prépare pour une course. Le premier jour de votre entrainement, vous courez _x_ kilomètres, et le jour de la course vous devrez être capable de courir _y_ kilomètres.

Écrivez un programme qui lit les nombres x et y dans cet ordre et affiche le nombre de jours d'entrainements requis pour atteindre le but y sachant que vous augmentez votre distance d'entrainement  10% chaque jour.

## **Exemple d'entrée**

```
10
30
```

## **Exemple de sortie**

```
13
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

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
x = int(input())
y = int(input())
num_days = 1
while x < y:
  x *= 1.1
  num_days += 1
print(num_days)
```
````
