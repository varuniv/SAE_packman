"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module case.pyd
        Ce module contient l'implémentation des cases du plateau de jeus
"""
import const 

def Case(mur=False, objet=const.AUCUN, pacmans_presents=None, fantomes_presents=None):
    """Permet de créer une case du plateau

    Args:
        mur (bool, optional): un booléen indiquant si la case est un mur ou un couloir.
                Defaults to False.
        objet (str, optional): un caractère indiquant l'objet qui se trouve sur la case.
                const.AUCUN indique qu'il n'y a pas d'objet sur la case. Defaults to const.AUCUN.
        pacmans_presents (set, optional): un ensemble indiquant la liste des pacmans
                se trouvant sur la case. Defaults to None.
        fantomes_presents (set, optional): un ensemble indiquant la liste des fantomes
                se trouvant sur la case. Defaults to None.

    Returns:
        dict: un dictionnaire représentant une case du plateau
    """
    if pacmans_presents == None:   #Si il n'y a aucun pacman présents 
        pacmans_presents = set()         #On crée un ensemble vide
    if fantomes_presents == None:    #Si il n'y a aucun fantomes présents 
        fantomes_presents = set()       #On crée un ensemble vide
    return {'mur': mur, 'objet':objet, 'pacman':pacmans_presents, 'fantome':fantomes_presents}   #On renvoie la case créée avec les différentes clés 



def est_mur(case):
    """indique si la case est un mur ou non

    Args:
        case (dict): la case considérée

    Returns:
        bool: True si la case est un mur et False sinon
    """
    return case['mur']       #récupère le booleen de la clé 'mur' dans la case, si il est à False alors cela renvoie False, True sinon




def get_objet(case):
    """retourne l'identifiant de l'objet qui se trouve sur la case. const.AUCUN indique l'absence d'objet.

    Args:
        case (dict): la case considérée

    Returns:
        str: l'identifiant de l'objet qui se trouve sur la case.
    """
    return case['objet']   #récupère le booleen de la clé 'objet' dans la case, si il est à False alors cela renvoie False, True sinon


def get_pacmans(case):
    """retourne l'ensemble des pacmans qui sont sur la case

    Args:
        case (dict): la case considérée

    Returns:
        set: l'ensemble des identifiants de pacmans présents su la case.
    """
    return case['pacman']     #récupère le booleen de la clé 'pacman' dans la case, si il est à False alors cela renvoie False, True sinon

def get_fantomes(case):
    """retourne l'ensemble des fantomes qui sont sur la case

    Args:
        case (dict): la case considérée

    Returns:
        set: l'ensemble des identifiants de fantomes présents su la case.
    """
    if case != None :
        return case['fantome']  #récupère le booleen de la clé 'fantome' dans la case, si il est à False alors cela renvoie False, True sinon
    else :
        return set()

def get_nb_pacmans(case):
    """retourne le nombre de pacmans présents sur la case

    Args:
        case (dict): la case considérée

    Returns:
        int: le nombre de pacmans présents sur la case.
    """
    return len(get_pacmans(case))        #récupère la taille de ce que retourne la fonction get_pacmans qui renvoie l'ensemble de tous les pacmans 

def get_nb_fantomes(case):
    """retourne le nombre de fantomes présents sur la case

    Args:
        case (dict): la case considérée

    Returns:
        int: le nombre de fantomes présents sur la case.
    """
    return len(get_fantomes(case))    #récupère la taille de ce que retourne la fonction get_pacmans qui renvoie l'ensemble de tous les pacmans 


def poser_objet(case, objet):
    """Pose un objet sur la case. Si un objet était déjà présent ce dernier disparait.
        Si la case est un mur, l'objet n'est pas mis dans la case.

    Args:
        case (dict): la case considérée
        objet (str): identifiant d'objet. const.AUCUN indiquant que plus aucun objet se
                trouve sur la case.
    """
    if not est_mur(case):           #si il n'y pas de mur à la case où l'on veut poser l'objet alors
        case['objet'] = objet       #On metl'objet à la clé objet car si un objet était déjà présent, il disparaît (on écrase sa mémoire)
    

def prendre_objet(case):
    """Enlève l'objet qui se trouve sur la case et retourne l'identifiant de cet objet.
        Si aucun objet se trouve sur la case la fonction retourne const.AUCUN.
 
    Args:
        case (dict): la case considérée

    Returns:
        char: l'identifiant de l'objet qui se trouve sur la case.
    """
    obj = get_objet(case)       #On récupère l'objet de la case 
    case['objet'] = const.AUCUN     #Et on modifie la valeur d'objet dans la case que l'on met à AUCUN
    return obj
    

def poser_pacman(case, pacman):
    """Pose un nouveau pacman sur la case.
    Si le pacman était déjà sur la case la fonction ne fait rien
    Si la case est un mur, le pacman est quand-même posé (pouvoir de passe-muraille)

    Args:
        case (dict): la case considérée
        pacman (str): identifiant du pacman à ajouter sur la case
    """
    case['pacman'].add(pacman)  #On ajoute à l'ensemble des pacmans de la case le pacman en paramètre de la fonction 
   
   

def prendre_pacman(case, pacman):
    """Enlève le pacman dont l'identifiant est passé en paramètre de la case.
        La fonction retourne True si le joueur était bien sur la case et False sinon.

    Args:
        case (dict): la case considérée
        pacman (str): l'identifiant du pacman à enlever

    Returns:
        bool: True si le joueur était bien sur la case et False sinon.
    """
    present =  pacman in get_pacmans(case)     #Si le pacman est dans l'ensemble des pacmans du plateau alors present est à True sinon present est à False
    case['pacman'] -= set(pacman)   #Enlève le pacman de l'ensemble des pacmans            
    return present

def poser_fantome(case, fantome):
    """Pose un nouveau fantome sur la case
        si le fantome était déjà sur la case, la fonction ne fait rien
        si la case est un mur la fonction ne fait rien

    Args:
        case (dict): la case considérée
        fantome (str): identifiant du fantome à ajouter sur la case
    """
    if not est_mur(case):           #si il n'y pas de mur à la case où l'on veut poser le fantome alors   
        case['fantome'].add(fantome)     #On ajoute le fantome à l'ensemble de fantomes de la case
   


def prendre_fantome(case, fantome):
    """Enlève le fantome dont l'identifiant est passé en paramètre de la case.
        La fonction retourne True si le fantome était bien sur la case et False sinon.

    Args:
        case (dict): la case considérée
        fantome (str): l'identifiant du fantome à enlever

    Returns:
        bool: True si le fantome était bien sur la case et False sinon.
    """
    present =  fantome in get_fantomes(case)  #Si le fantome est dans l'ensemble des fantomes du plateau alors present est à True sinon present est à False
    case['fantome'] -= set(fantome)    #Enlève le fantome de l'ensemble des fantomes
    return present
