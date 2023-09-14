# 1.4. Input/print: Précédent et suivant

## Consigne

Écrire un programme qui lit un nombre entier et affiche le nombre précédent et le nombre suivant (Cf. exemple ci-dessous).

## Exemple d'entrée

```
179
```

## Exemple de sortie

```
Le nombre suivant 179 est 180
Le nombre précédant 179 est 178
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
n = int(input())
print('Le nombre suivant ' + str(n) + ' est ' + str(n + 1))
print('Le nombre précédant ' + str(n) + ' est ' + str(n - 1))
```
````