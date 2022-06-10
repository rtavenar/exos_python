# 1.3. Input/print: Hello, Harry!

## Consigne

Écrire un programme qui accueille les utilisateurs avec 'Hello', une virgule, le prénom de l'utilisateur et un point d'exclamation à la fin. Cf. exemple ci-dessous.

**Attention :** La sortie de votre programme doit correspondre strictement à la description ci-dessus. Il n'y a pas d'espace entre le point d'exclamation et le prénom. Vous pouvez utiliser l'opérateur "+" pour concaténer deux chaînes de caractères.

## Exemple d'entrée

```
Harry
```

## Exemple de sortie

```
Hello, Harry!
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '1.3.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères:\n# a = input()\n# Afficher une chaîne de caractères:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print('Hello, ' + input() + '!')
```
````
