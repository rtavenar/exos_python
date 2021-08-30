from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  
# Écrire votre code ci-dessous
# Le périmètre d'un cercle de rayon R est égal à 2*pi*R

monCercle = Cercle(10)
perimetre = 2*pi*monCercle.rayon