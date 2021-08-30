angle_heures = int(input())   # angle de déplacement de l'aiguille des heures
nbh = angle_heures // 30      # l'aig des heures avance de 30° par h (360/12)
degh = angle_heures % 30      # est l'avancement de l'aig des heures pour les minutes
nbm = degh * 2                # l'aig des h avance 1° toutes les 2 mn (60/30)
angle_minutes = nbm * 6       # l'aig des mn avance de 6 ° par minute (360/60)
# print("nbh :", nbh, "nbm : ", nbm)
print(angle_minutes)