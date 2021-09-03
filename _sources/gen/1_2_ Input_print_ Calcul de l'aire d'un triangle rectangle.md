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

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lecture des nombres b et h comme ci-dessous :\nb = int(input())\n\n# Afficher le résultat avec : print()\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
b = int(input())
h = int(input())
print(b * h / 2)
```
````
