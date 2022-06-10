# 2.8. Nombres : siècle

## Consigne

Étant donnée une année (entrée au clavier comme un entier positif) trouver et afficher le siècle correspondant. Noter que, par exemple, le 20ème siècle commence avec l'année 1901.

## Example input

```
2000
```

## Example output

```
20
```

## Theory

If you don't know how to start solving this assignment, please, review a theory for this lesson:

https://snakify.org/lessons/integer_float_numbers/


You may also try step-by-step theory chunks:

https://snakify.org/lessons/integer_float_numbers/steps/1/

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.8.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print((a - 1) // 100 + 1)
```
````
