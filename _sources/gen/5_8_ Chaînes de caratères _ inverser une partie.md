# 5.8. Chaînes de caratères : inverser une partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, inverser la séquence de caractères se trouvant entre la première et la dernière occurrence de `h`.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In th a devil ereht dnuorg eht ni eloh ehobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle[::-1] + right)
```
````
