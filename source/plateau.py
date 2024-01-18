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
    if position_y - 1  < 0 :
        return (position_x,plateau['nb_colonnes']-1)
    return (position_x,position_y- 1)


def pos_est(plateau, pos):
    """retourne la position de la case à l'est de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    position_x, position_y = pos
    if position_y + 1 > plateau['nb_colonnes'] - 1:
        return (position_x,0)
    return (position_x  ,position_y +1) 



def pos_nord(plateau, pos):
    """retourne la position de la case au nord de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    (position_x,position_y) = pos
    if position_x - 1 < 0 :
        return (plateau['nb_lignes']-1, position_y)
    return (position_x-1,position_y)

def pos_sud(plateau, pos):
    """retourne la position de la case au sud de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    (position_x,position_y) = pos
    if position_x + 1 > plateau['nb_lignes'] - 1:
        return (0,position_y) 
    return (position_x + 1,position_y) 


def pos_arrivee(plateau, pos, direction):
    """Calcule la position d'arrivée si on part de pos et qu'on va dans
    la direction indiquée en tenant compte que le plateau est un tore.
    Si la direction n'existe pas, la fonction retourne None.

    Args:
        plateau (dict): Le plateau considéré.
        pos (tuple): Une paire d'entiers qui donne la position de départ.
        direction (str): Un des caractères NSEO donnant la direction du déplacement.

    Returns:
        None | tuple: None ou une paire d'entiers indiquant la position d'arrivée.
    """
    new_pos = None
    if direction == 'O':
        new_pos = pos_ouest(plateau, pos)
    elif direction == 'E':
        new_pos = pos_est(plateau, pos)
    elif direction == 'N':
        new_pos = pos_nord(plateau, pos)
    elif direction == 'S':
        new_pos = pos_sud(plateau, pos)
    return new_pos
    
    
    

def get_case(plateau, pos):
    """retourne la case qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        dict: La case qui se situe à la position pos du plateau
    """
    #print('plateau' in plateau.keys())
    
    return plateau['plateau'][pos]
    


def est_mur(plateau,pos): #Le S, function sup
    """indique si la case dans la pos est un mur ou non

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si la case est un mur et False sinon
    """
    return case.est_mur(get_case(plateau,pos))   # nous renvoie si la case est un mur.


def get_objet(plateau, pos):
    """retourne l'objet qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        str: le caractère symbolisant l'objet
    """
    return case.get_objet(get_case(plateau,pos))

def poser_pacman(plateau, pacman, pos):
    """pose un pacman en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le pacman
        pos (tuple): une paire (lig,col) de deux int
    """
    
    la_case = get_case(plateau,pos)
    la_case["pacman"].add(pacman)
    

def poser_fantome(plateau, fantome, pos):
    """pose un fantome en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int
    """
    case.poser_fantome(get_case(plateau,pos),fantome)
    
    
def poser_objet(plateau, objet, pos):
    """Pose un objet en position pos sur le plateau. Si cette case contenait déjà
        un objet ce dernier disparait

    Args:
        plateau (dict): le plateau considéré
        objet (int): un entier représentant l'objet. const.AUCUN indique aucun objet
        pos (tuple): une paire (lig,col) de deux int
    """
    return case.poser_objet(get_case(plateau,pos),objet)

    
def Plateau(la_chaine, complet=True):
    """Construit un plateau à partir d'une chaine de caractère contenant les informations
        sur le contenu du plateau (voir sujet)

    Args:
        la_chaine (str): la chaine de caractères décrivant le plateau

    Returns:
        dict: le plateau correspondant à la chaine. None si l'opération a échoué
    """
    plateau = {}    
    nouvelle_chaine = la_chaine.split("\n")   #On découpe le fichier en ligne
    
    distances = nouvelle_chaine[0].split(";")   #On s'occupe de trouver le nombre de lignes et colonnes indiqués au début
    nb_lignes = int(distances[0])
    nb_colonnes = int(distances[1])
    
    nouvelle_chaine = nouvelle_chaine[1:]   #On oublie pas d'enlever l'information déjà utilisée
    
    i = -1
    res = False
    while not res and i < len(nouvelle_chaine) :   #On récupère les infos du plateau et on les séparent en 2 grandes parties
        i = i+1
        if nouvelle_chaine[i][0] in '1234567890':
            res = True
            cases = nouvelle_chaine[:i]      #les cases du plateau
            donnees_persos = nouvelle_chaine[i:-1]   #les personnages disposés sur le plateau
    
    for val in range(2):    #On sépare les infos des pacmen et des fantômes
        if val == 0 :     #première partie = infos pacmen
            nb = int(donnees_persos[0])      
            pacmans = donnees_persos[1:nb+1]
            donnees_persos = donnees_persos[nb+1:] 
        else :                                        #Deuxième partie = infos fantômes
            nb = int(donnees_persos[0])
            fantomes = donnees_persos[1:nb+1]
            

    for ligne in range(nb_lignes):           #On ajoute au plateau les données telles que les coordonnées en clés & la présence mur ou d'objets
        for colonne in range(nb_colonnes):
            valeur = cases[ligne][colonne]
            if valeur == "#" :
                temp = case.Case(True)
            elif valeur in const.LES_OBJETS:
                temp = case.Case(False, valeur)
            else :
                temp = case.Case()   
            plateau[(ligne, colonne)] = temp    #le dictionnaire est construit au fur et à mesure

        
    for pac in pacmans :      #On ajoute les pacmans sur le plateau
        liste_donnees_p = pac.split(";")
        nom_p = liste_donnees_p[0]
        pos_p = (int(liste_donnees_p[1]), int(liste_donnees_p[2]))
        plateau[(pos_p[0], pos_p[1])]['pacman'].add(nom_p)
        
    for fan in fantomes :    #On ajoute les fantômes sur le plateau
        liste_donnees_f = fan.split(";")
        nom_f = liste_donnees_f[0]
        pos_f = (int(liste_donnees_f[1]), int(liste_donnees_f[2]))
        plateau[(pos_f[0], pos_f[1])]['fantome'].add(nom_f)
        
    dico_final = {'nb_lignes': nb_lignes, 'nb_colonnes' : nb_colonnes, 'plateau' : plateau}     #dico plateau de la forme : {(ligne, colonne) : {case}}
    return dico_final  
                                        #plateau = {'fantome': set(), 'mur': False, 'objet': '.', 'pacman': {'B'}}, pacman = 'B', pos = (1, 7)

def set_case(plateau, pos, une_case):
    """remplace la case qui se trouve en position pos du plateau par une_case

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int
        une_case (dict): la nouvelle case
    """
    plateau['plateau'][pos] = une_case

def enlever_pacman(plateau, pacman, pos): #Lenny
    """enlève un joueur qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le joueur
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    la_case = get_case(plateau, pos)

    if 'pacman' in la_case and str(pacman) in la_case['pacman']:
        la_case['pacman'].remove(str(pacman))
        set_case(plateau, pos, la_case)
        return True
    else:
        return False


def enlever_fantome(plateau, fantome, pos):
    """enlève un fantome qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    la_case = get_case(plateau, pos)
    if 'fantome' in la_case and str(fantome) in la_case['fantome']:
        la_case['fantome'].remove(str(fantome))
        set_case(plateau, pos, la_case)
        return True
    else:
        return False
    

def prendre_objet(plateau, pos):
    """Prend l'objet qui se trouve en position pos du plateau et retourne l'entier
        représentant cet objet. const.AUCUN indique qu'aucun objet se trouve sur la case

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
    
    la_case = get_case(plateau,pos)       
    if not pacman in case.get_pacmans(la_case):
        return None
    pos_arrive = pos_arrivee(plateau,pos,direction)
    if est_mur(plateau,pos_arrive):
        if passemuraille:
            case.prendre_pacman(la_case,pacman)      
            poser_pacman(plateau,pacman,pos_arrive)
            return pos_arrive
        else:
            return None
    else :
        case.prendre_pacman(la_case,pacman)
        poser_pacman(plateau,pacman,pos_arrive) 
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
    if fantome not in case.get_fantomes(get_case(plateau,pos)):
        return None
    
    pos_a = pos_arrivee(plateau,pos,direction)
    if est_mur(plateau,pos_a):
        return None
    case.prendre_fantome(get_case(plateau,pos),fantome)
    poser_fantome(plateau,fantome,pos_a)
    return pos_a

def case_vide(plateau):  #Lenny
    """choisi aléatoirement sur la plateau une case qui n'est pas un mur et qui
       ne contient ni pacman ni fantome ni objet

    Args:
        plateau (dict): le plateau

    Returns:
        (int,int): la position choisie
    """
    nb_colonnes = get_nb_colonnes(plateau)
    nb_lignes = get_nb_lignes(plateau)
    arret = False
    while not arret: 
        x = random.randint(0,len(nb_colonnes)-1)
        y = random.randint(0,len(nb_lignes)-1)   
        une_case = get_case(plateau,(x,y))
        if not case.est_un_mur(une_case) and case.get_nb_fantomes(une_case) == 0 and case.get_nb_pacmans(une_case) == 0 and case.get_objet(une_case) == const.AUCUN : 
            arret = True 
            
    return (x,y)


                
                
    


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
    if passemuraille:
        return directions
    for dir in directions:
        pos_posibble = pos_arrivee(plateau,pos,dir)
        if not est_mur(plateau,pos_posibble):
            res += dir           
    return res


     
#---------------------------------------------------------#

def analyse_plateau(plateau, pos, direction, distance_max):
    """calcul les distances entre la position pos est les differents objets et
        joueurs du plateau si on commence par partir dans la direction indiquee
        en se limitant a la distance max. Si il n'est pas possible d'aller dans la
        direction indiquee a partir de pos, la fonction doit retourner None

    Args:
        plateau (dict): le plateau considere
        pos (tuple): une paire d'entiers indiquant la postion de calcul des distances
        distance_max (int): un entier indiquant la distance limite de la recherche
    Returns:
        dict: un dictionnaire de listes. 
                Les cles du dictionnaire sont 'objets', 'pacmans' et 'fantomes'
                Les valeurs du dictionnaire sont des listes de paires de la forme
                    (dist,ident) ou dist est la distance de l'objet, du pacman ou du fantome
                                    et ident est l'identifiant de l'objet, du pacman ou du fantome
            S'il n'est pas possible d'aller dans la direction indiquee a partir de pos
            la fonction retourne None
    """
    #'N':{'objets': [(2, '@'), (3, '!'), (3, '.'), (3, '.'), (4, '.'), (4, '.'), (4, '.'), (5, '.'), (5, '.'), (5, '.'), (5, '~')],
    # 'pacmans': [(3, 'D'), (5, 'C')], 'fantomes': [(3, 'b'), (5, 'd')]}
    res = {'objets':[], 'pacmans':[], 'fantomes':[]}
    positions = {pos_arrivee(plateau,pos,direction)} 
    distance = 2
    while   distance-1 <= distance_max :
        vois = set()
        for p in positions:
            vois = vois.union(set([pos_arrivee(plateau,p,x) for x in directions_possibles(plateau,p)]))
        positions = set()
        for p in vois:
            if not est_mur(plateau,p) :
                la_case = get_case(plateau,p)
                positions.add(p)
                fantomes = case.get_fantomes(la_case)
                for fant in fantomes:
                    
                    res['fantomes'].append((distance,fant)) 
                pacman = case.get_pacmans(la_case)
                for pac in pacman:
        
                    res['pacmans'].append((distance,pac)) 
                obj = case.get_objet(la_case)
                if const.AUCUN != obj:
                    
                    res['objets'].append((distance,obj))
        distance +=1
    return res
         




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
    
    distance = 0
    dirc_prec = directions_possibles(plateau, pos)
    proch_pos = pos_arrivee(plateau, pos, direction)
    dirc = directions_possibles(plateau, proch_pos)
    nb_dirc = len(dirc) 
    while nb_dirc <= 2:
        nb_dirc = len(dirc) 
        if nb_dirc >= 3:
            return distance
        if nb_dirc <= 1:
            return -1
        if nb_dirc == 2 :
            if direction not in dirc:
                dirc = set(dirc)
                setdirc = dirc.difference(set(dirc_prec))
                for d in setdirc:
                    direction = d
        distance += 1
        proch_pos = pos_arrivee(plateau, proch_pos, direction)
        dirc_prec = dirc
        dirc = directions_possibles(plateau, proch_pos)
    if nb_dirc == 0:
        return -1  
    return  distance 
    

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


