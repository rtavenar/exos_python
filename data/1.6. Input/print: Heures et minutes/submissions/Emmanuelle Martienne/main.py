# Saisie du nombre de secondes écoulées depuis minuit
nbsec = int(input())
nbheures = nbsec // 3600
nbmin = nbsec // 60
print("{0:d} {1:d}".format(nbheures,nbmin))