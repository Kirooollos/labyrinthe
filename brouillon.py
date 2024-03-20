
import random
from turtle import *
from PROJET_LABYRINTHE import carre, typeCellule

def generate_random_maze(laby_colone, laby_lignes):
  labyrinthe = []
  for i in range(laby_colone):
    sublist = []
    for j in range(laby_lignes):
      sublist.append(random.randint(0, 1))
    labyrinthe.append(sublist)
  return labyrinthe

laby =generate_random_maze(11,12)
print(generate_random_maze(11,12))

def afficheGraphique(labyrinthe, epaisseur):
    lignes = 0
    coorEntree = [10,0]
    coorSortie = [1, 11]
    xcor = -300
    ycor = 300
    tracer(0, 0)
    up()
    goto(xcor, ycor)
    down()
    for i in labyrinthe["labyrinthe"]:
      colonnes = 0
      for k in range(0, len(i)):
        if i[k] == 1:  # tracer les murs
          carre(epaisseur, "black", "black")
        elif i[k] == 0:
          if [lignes, colonnes] == coorEntree:  # tracer l'entree
            carre(epaisseur, "purple", "#222222")
          elif [lignes, colonnes] == coorSortie:  # tracer la sortie
            carre(epaisseur, "green", "#222222")
          else:  # blanc
            if typeCellule(lignes, colonnes) == "carrefour":
              carre(epaisseur, "yellow", "#222222")
            elif typeCellule(lignes, colonnes) == "impasse":
              carre(epaisseur, "gray", "black")
            else:
              carre(epaisseur, "white", "#222222")
        colonnes += 1
      ycor -= epaisseur  # mettre le cursus au début la nouvelle ligne
      up()
      goto(xcor, ycor)
      down()
      lignes += 1
    update()  # mettre a jour les nouvelles actions


print(generate_random_maze(3, 4))