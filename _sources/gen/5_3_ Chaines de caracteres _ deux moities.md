# 5.3. Chaînes de caractères : deux moitiés

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, la découper en deux parties égales. Si la longueur est impaire, garder le caractère du milieu dans le premier découpage de sorte que la première chaîne découpée contienne un caractère de plus que la seconde. Ensuite, afficher une nouvelle chaîne de caractères sur une seule ligne avec les deux parties découpées échangées : la seconde moitié en premier et la première moitié en dernier.

Peut-on résoudre le problème sans utiliser `if`?

## Exemple d'entrée

```
Qwerty
```

## Exemple de sortie

```
rtyQwe
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html#les-cha%C3%AEnes-de-caract%C3%A8res

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Lire une chaîne de caractères :
# s = input()
# Afficher une chaîne de caractères :
# print(s)
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
s = input()
mid = (len(s) + 1) // 2
print(s[mid:] + s[:mid])
```
````
