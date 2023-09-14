# A.8. Dicts: Dictionnaire Français-Latin

## Énoncé

Un jour, Bob trouve un dictionnaire Français-Latin dans son grenier. Lui qui voulait se mettre à apprendre le latin voit cela comme une superbe opportunité, mais il se dit qu'il aurait également besoin d'un autre dictionnaire : un dictionnaire Latin-Français. Votre but sera de l'aider à créer ce dictionnaire à partir des informations issues du dictionnaire Français-Latin.

La première ligne entrée au clavier sera un entier `N` — le nombre de mots du dictionnaire Français-Latin - suivi de `N` entrées de dictionnaire. Chaque entrée se trouve sur une ligne séparée et contient le mot en Français, un tiret puis la ou les traductions latines, séparées par des virgules s'il y en a plusieurs et triées dans l'ordre lexicographique.

Affichez le dictionnaire Latin-Français dans le même format. En particulier, les lignes seront triées dans l'ordre lexicographique du terme en latin, et pour un terme latin, les équivalents français seront triés eux-mêmes dans l'ordre lexicographique.

## Exemple d'entrée

```
2
pomme - malum, pomum
mauvais - malum, malus
```

## Exemple de sortie

```
3
malum - mauvais, pomme
malus - mauvais
pomum - pomme
```

## Aide

https://rtavenar.github.io/poly_python/content/dict.htmlhttps://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

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
la_en = {}
for _ in range(int(input())):
  en_word, la_words = input().split(' - ')
  for la_word in la_words.split(', '):
    if la_word not in la_en:
      la_en[la_word] = []
    la_en[la_word].append(en_word)
print(len(la_en))
for la_word in sorted(la_en):
  print(la_word, '-', ', '.join(sorted(la_en[la_word])))
```
````
