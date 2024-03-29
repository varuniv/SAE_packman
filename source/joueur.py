"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module joueur.py
        Ce module contient l'implémentation de la structure de données
        qui gère un joueur et ses caractéristiques 
"""
import const


def Joueur(couleur, nom, nb_points, nb_faux_mvt, pos_pacman, pos_fantome, objets):
    """Créer un nouveau joueur à partir de ses caractéristiques

    Args:
        couleur (str): une lettre majuscule indiquant la couleur du joueur
        nom (str): un nom de joueur
        nb_points (int): un entier qui indique le nombre de points du joueur
        nb_faux_mouvements (int): un entier qui indique le nombre de faux mouvements autorisés pour le joueur
        pos_pacman (tuple): une paire d'entiers indiquant sur quelle case se trouve le pacman du joueur
        pos_fantome (tuple): une paire d'entiers indiquant sur quelle case se trouve le fantome du joueur
        objets (dict): un dictionnaire indiquant la durée restante pour chaque objet du joueur

    Returns:
        dict: un dictionnaire représentant le joueur
    """
    dico_joueur = {"nom" : nom, "couleur" : couleur, "nb_points" : nb_points, "nb_faux_mvt" : nb_faux_mvt, "pos_pacman": pos_pacman, "pos_fantome": pos_fantome, "objets" : objets} 
    return dico_joueur
    #On crée un dictionnnaire contenant les différents attributs d'un joueur 


def joueur_from_str(description):
    """créer un joueur à partir d'un chaine de caractères qui contient
        ses caractéristiques séparées par des ; dans l'ordre suivant:
    "couleur;nb_points;nb_faux_mvt;lin_p;col_p;lin_f;col_f;duree_glout;duree_immo;duree_mur;nom_joueur"

    Args:
        description (str): la chaine de caractères contenant les caractéristiques
                            du joueur

    Returns:
        dict: le joueur ayant les caractéristiques décrite dans la chaine.
    """
    valeurs_j = description.split(";")
    dico_j = Joueur(valeurs_j[0], valeurs_j[10], int(valeurs_j[1]), int(valeurs_j[2]), (int(valeurs_j[3]), int(valeurs_j[4])), (int(valeurs_j[5]), int(valeurs_j[6])), {})
    if valeurs_j[7] != "0":
        dico_j["objets"]["$"] =  int(valeurs_j[7])
    if valeurs_j[8] != "0":
        dico_j["objets"]["@"] = int(valeurs_j[8])
    if valeurs_j[9] != "0":
        dico_j["objets"]["~"] = int(valeurs_j[9])
    return dico_j


def get_couleur(joueur):
    """retourne la couleur du joueur

    Args:
        joueur (dict): le joueur considéré

    Returns:
        str: une lettre indiquant la couleur du joueur
    """
    return joueur["couleur"]   #On récupère le couleur dans le dictionnaire joueur grâce à la clé 'couleur'


def get_nom(joueur):
    """retourne le nom du joueur

    Args:
        joueur (dict): le joueur considéré

    Returns:
        str: le nom du joueur
    """
    return joueur["nom"]


def get_nb_points(joueur):
    """retourne le nombre de points du joueur
    joueur (dict): le joueur considéré

    Returns:
        int: la réserve du joueur
    """
    return joueur["nb_points"]    #récupère la valeur de la clé 'nb_points'


def get_nb_faux_mvt(joueur):
    """retourne le nombre de faux mouvements autorisés pour le joueur
    joueur (dict): le joueur considéré

    Returns:
        int: le nombre de faux mouvements autorisés du joueur
    """
    return joueur["nb_faux_mvt"]    #récupère  la valeur de la clé 'nb_faux_mvt'


def get_objets(joueur):
    """retourne la liste des objets possédés par le joueur
    joueur (dict): le joueur considéré

    Returns:
        (list): la liste des objets possédés par le joueur
    """
    return list(joueur["objets"].keys())


def get_duree(joueur, objet):
    """retourne la duree de vie de l'objet possédé par le joueur
    joueur (dict): le joueur considéré
    objet (str): un identifiant d'objet

    Returns:
        int: un entier indiquant la durée de vie l'objet possédé par le joueur
            0 indique que le joueur n'a pas l'objet ou que celui-ci a une durée de vie de 0
    """
    if objet in joueur["objets"].keys():
        duree = joueur["objets"][objet]
    else :
        duree = 0
    return duree


def get_pos_pacman(joueur):
    """retourne la position du pacman du joueur. ATTENTION c'est la position stockée dans le
        pacman. On ne la calcule pas
    joueur (dict): le joueur considéré

    Returns:
        tuple: une paire d'entiers indiquant la position du pacman du joueur.
    """
    return joueur["pos_pacman"]


def get_pos_fantome(joueur):
    """retourne la position du fantome du joueur. ATTENTION c'est la position stockée dans le
        fantome. On ne la calcule pas
    joueur (dict): le joueur considéré

    Returns:
        tuple: une paire d'entiers indiquant la position du fantome du joueur.
    """
    return joueur["pos_fantome"]


def set_pos_pacman(joueur, pos):
    """met à jour la position du pacman du joueur

    Args:
        joueur (dict): le joueur considéré
        pos (tuple): une paire d'entiers (lin,col) indiquant la position du joueur
    """
    joueur["pos_pacman"] = pos


def set_pos_fantome(joueur, pos):
    """met à jour la position du fantome du joueur

    Args:
        joueur (dict): le joueur considéré
        pos (tuple): une paire d'entiers (lin,col) indiquant la position du joueur
    """
    joueur["pos_fantome"] = pos


def add_points(joueur, quantite):
    """ modifie le nombre de points du joueur.
        ATTENTION! La quantité ajoutée peut être négative et le total du joueur peut devenir négatif aussi

    Args:
        joueur (dict): le joueur considéré
        quantite (int): un entier positif ou négatif inquant la variation du nombre de points
    Returns:
        int: le nouveau nombre de points du joueur
    """
    joueur["nb_points"] += quantite
    return joueur["nb_points"]


def faux_mouvement(joueur):
    """Enlève 1 au nombre de faux mouvements autorisés pour le joueur

    Args:
        joueur (dict): le joueur considéré
    Returns:
        int: le nombre de faux mouvements autorisés restants
    """
    joueur["nb_faux_mvt"] -= 1
    return joueur["nb_faux_mvt"]


def reinit_faux_mouvements(joueur):
    """Réinitialise le nombre de faux mouvements autorisés pour le joueur

    Args:
        joueur (dict): le joueur considéré
    """
    joueur["nb_faux_mvt"] = 4


def ajouter_objet(joueur, objet):
    """ajoute un objet au joueur.
        La durée de vie de l'objet (si elle est supérieure à 0) est ajoutée
        Le nombre de points du joueur est mis à jour
        Les informations sur les objets sont stockées dans const.PROP_OBJET
    Args:
        joueur (dict): le joueur considéré
        objet (str): l'objet considéré
    """
    duree = const.PROP_OBJET[objet][1]
    points = const.PROP_OBJET[objet][0]
    if duree > 0 and objet in joueur["objets"].keys(): 
        joueur["objets"][objet] += duree
    else : 
        joueur["objets"][objet] = duree
    joueur["nb_points"] =  add_points(joueur, points)


def maj_duree(joueur):
    """décrémente la durée de vie des objets possédés par le joueur.
        Si la durée d'un objet est à 0 celle-ci reste à 0

    Args:
        joueur (dict): le joueur considéré
    """
    for objet in joueur["objets"]:
        duree = get_duree(joueur, objet)
        if duree > 0: 
            joueur["objets"][objet] -= 1
    

# A NE PAS DEMANDER
def joueur_2_str(joueur,separateur=";"):
        return str(joueur["couleur"])+separateur+str(joueur["nb_points"])+\
            separateur+str(joueur["nb_faux_mvt"])+separateur+\
            str(joueur["pos_pacman"][0])+separateur+str(joueur["pos_pacman"][1])+\
            separateur+str(joueur["pos_fantome"][0])+separateur+str(joueur["pos_fantome"][1])+\
            separateur+str(joueur["objets"][const.GLOUTON])+separateur+\
            str(joueur["objets"][const.IMMOBILITE])+separateur+\
            str(joueur["objets"][const.PASSEMURAILLE])+separateur+joueur["nom"]+'\n'
