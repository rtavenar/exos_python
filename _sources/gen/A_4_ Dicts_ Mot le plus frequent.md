# A.4. Dicts: Mot le plus fréquent

## Consigne

À partir d'un texte contenant n lignes, la première entrée correspondra au nombre de lignes n puis chaque ligne du texte sera entrée l'une après l'autre.

Affichez le mot le plus fréquent du texte. Si plusieurs mots ont la même fréquence, on choisira le premier du classement alphabétique.

## Exemple d'entrée

```
2
apple orange banana
banana orange
```

## Exemple de sortie

```
banana
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
words_count = {}
for i in range(int(input())):
  words = input().split()
  for word in words:
    if word not in words_count:
      words_count[word] = 0
    words_count[word] += 1
max_frequency = max(words_count.values())
for word in sorted(words_count):
  if words_count[word] == max_frequency:
    print(word)
    break
```
````