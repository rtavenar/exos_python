nb = int(input())

diviseur = 2
pastrouvé = True
while pastrouvé and (diviseur <= nb / 2):
  if nb % diviseur == 0:
    print(diviseur)
    pastrouvé = False
  else:
    diviseur += 1
if pastrouvé:
  print(nb)

# on évite de tester les valeurs entre nb/2 et nb qui ne sont pas diviseurs !