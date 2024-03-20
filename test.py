def labyFromFile(fn) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    Read a maze from the file named fn.
    """
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut


#navigation Test

import turtle as tt

#on doit d'abord creer un turtle object afin de le faire
object= carre(40, "purple")
def gauche():
    x = object.xcor()
    x -= 40
    object.setx(x)
    print("gauche ; left")


def droite():
    x= object.xcor()
    x += 40
    object.setx(x)
    print("droite ; right")


def bas():
    y = object.ycor()
    y -= 40
    object.sety(y)
    print("bas ; down")


def haut():
    y = object.ycor()
    y += 40
    object.sety(y)
    print("haut ; up")


# key bindings
tt.onkeypress(gauche, "Left")
tt.onkeypress(droite, "Right")
tt.onkeypress(haut, "Up")
tt.onkeypress(bas, "Down")
tt.listen()





