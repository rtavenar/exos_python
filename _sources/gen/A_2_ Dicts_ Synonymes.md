# A.2. Dicts: Synonymes

## Consigne

Soit un dictionnaire composé de paires de mots. Chaque mot est un synonyme de l'autre mot dans sa paire.

À partir d'une liste de paires de mots, vous devrez créer un tel dictionnaire.

À la suite du dictionnaire, l'utilisateur propose un mot en entrée pour obtenir le synonyme. La réponse sera la valeur correspondant à la clé (mot proposé en entrée).


## Exemple d'entrée

```
3
Hello Hi
Bye Goodbye
List Array
Goodbye
```

## Exemple de sortie

```
Bye
```

## Aide

https://rtavenar.github.io/poly_python/content/dict.html

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    # Read a string:
# s = input()
# Print a value:
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
synonyms = {}
for i in range(int(input())):
  w1, w2 = input().split()
  synonyms[w1] = w2
  synonyms[w2] = w1
print(synonyms[input()])
```
````
