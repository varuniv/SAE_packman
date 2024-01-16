"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module plateau.py
        Ce module contient l'implémentation de la structure de données
        qui gère le plateau jeu aussi qu'un certain nombre de fonctions
        permettant d'observer le plateau et d'aider l'IA à prendre des décisions
"""
import const
import case
import random



def get_nb_lignes(plateau):
    """retourne le nombre de lignes du plateau

    Args:
        plateau (dict): le plateau considéré

    Returns:
        int: le nombre de lignes du plateau
    """
    return plateau['nb_lignes']


def get_nb_colonnes(plateau):
    """retourne le nombre de colonnes du plateau

    Args:
        plateau (dict): le plateau considéré

    Returns:
        int: le nombre de colonnes du plateau
    """
    return plateau['nb_colonnes']

    

def pos_ouest(plateau, pos):
    """retourne la position de la case à l'ouest de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    (position_x,position_y) = pos
    return plateau[position_x-1,position_y] 

def pos_est(plateau, pos):
    """retourne la position de la case à l'est de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    (position_x,position_y) = pos
    return plateau[position_x+1,position_y] 

def pos_nord(plateau, pos):
    """retourne la position de la case au nord de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    (position_x,position_y) = pos
    return plateau[position_x,position_y-1] 

def pos_sud(plateau, pos):
    """retourne la position de la case au sud de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    (position_x,position_y) = pos
    return plateau[position_x,position_y+1] 



def pos_arrivee(plateau,pos,direction): #by Le S
    """ calcule la position d'arrivée si on part de pos et qu'on va dans
    la direction indiquée en tenant compte que le plateau est un tore
    si la direction n'existe pas la fonction retourne None
    Args:
        plateau (dict): Le plateau considéré
        pos (tuple): une paire d'entiers qui donne la position de départ
        direction (str): un des caractère NSEO donnant la direction du déplacement

    Returns:
        None|tuple: None ou une paire d'entiers indiquant la position d'arrivée
    """
    
    new_pos = None
    lgn_max = get_nb_lignes(plateau)-1
    col_max = get_nb_colonnes(plateau)-1
    borderline_gauche =  pos[1] == 0
    borderline_droite = pos[1] == col_max 
    borderline_top = pos[0] == 0 
    borderline_bas =  pos[0] == lgn_max
    match direction:
        case  'O':
            new_pos = pos_ouest(plateau,pos)
            if borderline_gauche:
                new_pos[1] = col_max
        case  'E':
            new_pos = pos_est(plateau,pos)
            if borderline_droite:
                new_pos[1] = 0
        case  'N':
            new_pos = pos_nord(plateau,pos)
            if borderline_top:
                new_pos[0] = lgn_max
        case  'S':
            new_pos = pos_sud(plateau,pos)
            if borderline_bas:
                new_pos[0] = 0
    if new_pos is None or new_pos not in plateau:
        return None
    return new_pos
    

    

def get_case(plateau, pos):
    """retourne la case qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        dict: La case qui se situe à la position pos du plateau
    """
    return plateau[pos]

def get_objet(plateau, pos):
    """retourne l'objet qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        str: le caractère symbolisant l'objet
    """
    return case.get_objet(get_case(plateau,pos))

def est_mur(plateau,pos): #Le S, function sup
    """indique si la case dans la pos est un mur ou non

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si la case est un mur et False sinon
    """
    return case.est_mur(get_case(plateau,pos))

def poser_pacman(plateau, pacman, pos):
    """pose un pacman en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le pacman
        pos (tuple): une paire (lig,col) de deux int
    """
    return case.poser_pacman(get_case(plateau,pos),pacman)


def poser_fantome(plateau, fantome, pos):
    """pose un fantome en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int
    """
    return case.poser_fantome(get_case(plateau,pos),fantome)

    
def poser_objet(plateau, objet, pos):
    """Pose un objet en position pos sur le plateau. Si cette case contenait déjà
        un objet ce dernier disparait

    Args:
        plateau (dict): le plateau considéré
        objet (int): un entier représentant l'objet. const.AUCUN indique aucun objet
        pos (tuple): une paire (lig,col) de deux int
    """
    return case.poser_objet(get_case(plateau,pos),objet)


def plateau(la_chaine, complet=True):
    """Construit un plateau à partir d'une chaine de caractère contenant les informations
        sur le contenu du plateau (voir sujet)

    Args:
        la_chaine (str): la chaine de caractères décrivant le plateau

    Returns:
        dict: le plateau correspondant à la chaine. None si l'opération a échoué
    """
    plateau = {}
    nouvelle_chaine = la_chaine.split("\n")[1:]
    i = -1
    res = False
    while not res and i < len(nouvelle_chaine) :
        i = i+1
        if nouvelle_chaine[i][0] in '0123456789':
            res = True
            cases = nouvelle_chaine[:i]
            donnees_persos = nouvelle_chaine[i:-1]

    tours = 0
    for donnees in donnees_persos :
        tours += 1
        if tours < 2 :
            nb = int(donnees)
            pacmans = donnees_persos[1:nb+1]
            donnees_persos = donnees_persos[nb+1:]
        else :
            nb = int(donnees)
            fantomes = donnees_persos[1:nb+1]
    
    tt_cases = []
    nb_lignes = 0
    for lin in cases :
        nb_lignes += 1
        for caractere in lin :

            if caractere == "#":
                temp = case.Case(True,...)
            elif caractere == const.LES_OBJETS:
                temp = case.Case(False, caractere, ... )
            else :
                temp = case.Case(False,...,)
            tt_cases.append(temp)

        plateau[nb_lignes] = tt_cases

    for pac in pacmans :
        liste_donnees_p = pac.split(";")
        nom_p = liste_donnees_p[0]
        pos_p = tuple(int(liste_donnees_p[1]), int(liste_donnees_p[2]))
        plateau[pos_p[0]][pos_p[1]]['pacman'].add(nom_p)
        
    for fan in fantomes :
        liste_donnees_f = fan.split(",")
        nom_f = liste_donnees_f[0]
        pos_f = tuple(int(liste_donnees_f[1]), int(liste_donnees_f[2]))
        plateau[pos_f[0]][pos_f[1]]['fantome'].add(nom_f)

    return plateau
    
    
    
    

#plateau {1: [{case1}, {case2}], 2: [{case1},{case2}]}
    

 


def set_case(plateau, pos, une_case):
    """remplace la case qui se trouve en position pos du plateau par une_case

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int
        une_case (dict): la nouvelle case
    """
    ancienne_case = get_case(plateau, pos) 
    ancienne_case = une_case
    return ancienne_case


def enlever_pacman(plateau, pacman, pos):
    """enlève un joueur qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le joueur
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    la_case = get_case(plateau,pos)
    case.prendre_pacman(la_case['pacman'], pacman)
    return pacman in la_case['pacman']
    
    
    
    
    


def enlever_fantome(plateau, fantome, pos):
    """enlève un fantome qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    la_case = get_case(plateau,pos)
    case.prendre_fantome(la_case['fantome'], fantome)
    return fantome in la_case['fantome']



def prendre_objet(plateau, pos):
    """Prend l'objet qui se trouve en position pos du plateau et retourne l'entier
        représentant cet objet. const.AUCUN indique qu'aucun objet se trouve sur case

    Args:
        plateau (dict): Le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        int: l'entier représentant l'objet qui se trouvait sur la case.
        const.AUCUN indique aucun objet
    """
    return case.prendre_objet(get_case(plateau,pos))


def deplacer_pacman(plateau, pacman, pos, direction, passemuraille=False): 
    """Déplace dans la direction indiquée un joueur se trouvant en position pos
        sur le plateau si c'est possible

    Args:
        plateau (dict): Le plateau considéré
        pacman (str): La lettre identifiant le pacman à déplacer
        pos (tuple): une paire (lig,col) d'int
        direction (str): une lettre parmie NSEO indiquant la direction du déplacement
        passemuraille (bool): un booléen indiquant si le pacman est passemuraille ou non

    Returns:
        (int,int): une paire (lig,col) indiquant la position d'arrivée du pacman 
                   (None si le pacman n'a pas pu se déplacer)
    """
    
    pos_arrive = pos_arrivee(plateau,pos,direction)
    la_case = get_case(plateau,pos_arrive)
    if est_mur(plateau,pos_arrive):
        if passemuraille == False :
            return None
        elif passemuraille == True : 
            poser_pacman(la_case,pacman)
            return pos_arrive
    else :
            poser_pacman(la_case,pacman) 
            return pos_arrive      

def deplacer_fantome(plateau, fantome, pos, direction): #Lucas
    """Déplace dans la direction indiquée un fantome se trouvant en position pos
        sur le plateau

    Args:
        plateau (dict): Le plateau considéré
        fantome (str): La lettre identifiant le fantome à déplacer
        pos (tuple): une paire (lig,col) d'int
        direction (str): une lettre parmie NSEO indiquant la direction du déplacement

    Returns:
        (int,int): une paire (lig,col) indiquant la position d'arrivée du fantome
                   None si le joueur n'a pas pu se déplacer
    """
    pos_arrive = pos_arrivee(plateau,pos,direction)
    la_case = get_case(plateau,pos_arrive)
    if est_mur(plateau,pos_arrive):
         return None
    else :
            poser_pacman(la_case,fantome) 
            return pos_arrive     

def case_vide(plateau): #Lenny
    """choisi aléatoirement sur la plateau une case qui n'est pas un mur et qui
       ne contient ni pacman ni fantome ni objet

    Args:
        plateau (dict): le plateau

    Returns:
        (int,int): la position choisie
    """

    nb_lignes_plateau = get_nb_lignes(plateau)
    nb_colonnes_plateau = get_nb_colonnes(plateau)    
    catalogue = []    
    for x in range(nb_lignes_plateau):
        for y in range(nb_colonnes_plateau):
            une_case = get_case(plateau,(x,y))
            if not case.est_un_mur(une_case) and case.get_nb_fantomes(une_case) == 0 and case.get_nb_pacmans(une_case) == 0: 
                catalogue.append((x,y))
    indice_pos_finale = random.randint(0,len(catalogue)-1)
    return catalogue[indice_pos_finale] 


def directions_possibles(plateau,pos,passemuraille=False):# by Le S 
    """ retourne les directions vers où il est possible de se déplacer à partir
        de la position pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): un couple d'entiers (ligne,colonne) indiquant la position de départ
        passemuraille (bool): indique si on s'autorise à passer au travers des murs
    
    Returns:
        str: une chaine de caractères indiquant les directions possibles
              à partir de pos
    """
    directions = 'NESO'
    res = ''
    for dir in directions:
        pos_posibble = pos_arrivee(plateau,pos,dir)
        if not pos_posibble is None:
            if passemuraille :
                res += dir
            else:
                if not est_mur(plateau,pos):
                    res += dir 
    return res
#---------------------------------------------------------#


def analyse_plateau(plateau, pos, direction, distance_max): #Sargis 
    """calcul les distances entre la position pos est les différents objets et
        joueurs du plateau si on commence par partir dans la direction indiquée
        en se limitant à la distance max. Si il n'est pas possible d'aller dans la
        direction indiquée à partir de pos, la fonction doit retourner None

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers indiquant la postion de calcul des distances
        distance_max (int): un entier indiquant la distance limite de la recherche
    Returns:
        dict: un dictionnaire de listes. 
                Les clés du dictionnaire sont 'objets', 'pacmans' et 'fantomes'
                Les valeurs du dictionnaire sont des listes de paires de la forme
                    (dist,ident) où dist est la distance de l'objet, du pacman ou du fantome
                                    et ident est l'identifiant de l'objet, du pacman ou du fantome
            S'il n'est pas possible d'aller dans la direction indiquée à partir de pos
            la fonction retourne None
    """
    nb_lignes = get_nb_lignes(plateau)
    nb_colonnes =get_nb_colonnes(plateau)

    res = {'objets':[] , 'pacmans':[] , 'fantomes': []}
    distance = 0
    ident = 0
    dir = directions_possibles(plateau,pos)
    while distance < distance_max and direction in dir:
        
        ...


def prochaine_intersection(plateau,pos,direction):  #Lenny / Sargis
    """calcule la distance de la prochaine intersection
        si on s'engage dans la direction indiquée

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position de départ
        direction (str): la direction choisie

    Returns:
        int: un entier indiquant la distance à la prochaine intersection
             -1 si la direction mène à un cul de sac.
    """
    proch_pos =pos_arrivee(plateau,pos,direction) #on avance
    dirc = directions_possibles(plateau,proch_pos) #les chemains possible
    nb_dirc = len(dirc) -1 #le nb de chemains moins d'ou on viens
    distance = 1    #
    if nb_dirc == 0:
        return -1 
    if nb_dirc > 1:
        return distance
    else: #1 chemin possible, len de dirc == 2 
        if direction in dirc:
            inter = prochaine_intersection(plateau,proch_pos,direction)
            if inter == -1:
                return -1
            else:
                return distance + inter
        else:
            inverse = 'SONE'
            i_inverse = dirc.find(direction)
            d = inverse[i_inverse] 
            if dirc[0] == d :
                d = dirc[1]
            else:
                d = dirc[0]
            inter = prochaine_intersection(plateau,proch_pos,d)
            if inter == -1:
                return -1
            else:
                return distance + inter


    


#une chaine de caractères indiquant les directions possibles
              #à partir de pos   

# A NE PAS DEMANDER
def plateau_2_str(plateau):
        res = str(get_nb_lignes(plateau))+";"+str(get_nb_colonnes(plateau))+"\n"
        pacmans = []
        fantomes = []
        for lig in range(get_nb_lignes(plateau)):
            ligne = ""
            for col in range(get_nb_colonnes(plateau)):
                la_case = get_case(plateau,(lig, col))
                if case.est_mur(la_case):
                    ligne += "#"
                    les_pacmans = case.get_pacmans(la_case)
                    for pac in les_pacmans:
                        pacmans.append((pac, lig, col))
                else:
                    obj = case.get_objet(la_case)
                    les_pacmans = case.get_pacmans(la_case)
                    les_fantomes= case.get_fantomes(la_case)
                    ligne += str(obj)
                    for pac in les_pacmans:
                        pacmans.append((pac, lig, col))
                    for fantome in les_fantomes:
                        fantomes.append((fantome,lig,col))
            res += ligne+"\n"
        res += str(len(pacmans))+'\n'
        for pac, lig, col in pacmans:
            res += str(pac)+";"+str(lig)+";"+str(col)+"\n"
        res += str(len(fantomes))+"\n"
        for fantome, lig, col in fantomes:
            res += str(fantome)+";"+str(lig)+";"+str(col)+"\n"
        return res

