# coding: utf-8
"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module client_joueur.py
        Ce module contient le programme principal d'un joueur
        il s'occupe des communications avec le serveur
            - envois des ordres
            - recupération de l'état du jeu
        la fonction mon_IA est celle qui contient la stratégie de
        jeu du joueur.

"""
import argparse
import random
import client
import const
import plateau
import case
import joueur

prec='X'

def mon_IA(ma_couleur,carac_jeu, plan, les_joueurs):
    """ Cette fonction permet de calculer les deux actions du joueur de couleur ma_couleur
        en fonction de l'état du jeu décrit par les paramètres. 
        Le premier caractère est parmi XSNOE X indique pas de peinture et les autres
        caractères indique la direction où peindre (Nord, Sud, Est ou Ouest)
        Le deuxième caractère est parmi SNOE indiquant la direction où se déplacer.

    Args:
        ma_couleur (str): un caractère en majuscule indiquant la couleur du jeur
        carac_jeu (str): une chaine de caractères contenant les caractéristiques
                                   de la partie séparées par des ;
             duree_act;duree_tot;reserve_init;duree_obj;penalite;bonus_touche;bonus_rechar;bonus_objet           
        plan (str): le plan du plateau comme comme indiqué dans le sujet
        les_joueurs (str): le liste des joueurs avec leur caractéristique (1 joueur par ligne)
        couleur;reserve;nb_cases_peintes;objet;duree_objet;ligne;colonne;nom_complet
    
    Returns:
        str: une chaine de deux caractères en majuscules indiquant la direction de peinture
            et la direction de déplacement
    """
    # decodage des informations provenant du serveur
    joueurs={}
    for ligne in les_joueurs.split('\n'):
        lejoueur=joueur.joueur_from_str(ligne)
        joueurs[joueur.get_couleur(lejoueur)]=lejoueur
    le_plateau=plateau.Plateau(plan)
    
    #Instructions pacmans et fantômes

    def zone_definie(plat, pos_depart, valeur) :   #A tester
        """ Défini une zone précise accessible par le fantôme et le pacman
        
        Args():
            plat(dict): le plateau sous forme de dictionnaire
            pos_depart(tuple): la position du joueur (ligne, colonne)
            

        Returns :
            (list) : une liste de tuples avec toutes les positions concernées par le périmètre
        """
        actuelle = [pos_depart]
        pos_arrivee = []
        val = 0
        while val < valeur :
            temp = []
            val += 1
            for pos in actuelle :
                direction = plateau.directions_possibles(plat['plateau'], pos)
                for dir in direction :
                    case = plateau.pos_arrivee(plat['plateau'], pos, dir)
                    if not case in pos_arrivee :
                        temp.append(case)
                pos_arrivee = pos_arrivee + temp
            actuelle = temp

        return pos_arrivee 
    

    def zone_definie_avec_pass(plat, pos_depart, valeur) :   #A tester
        """ Défini une zone précise accessible par le pacman muni d'un passemuraille
        
        Args():
            plat(dict): le plateau sous forme de dictionnaire
            pos_depart(tuple): la position du joueur (ligne, colonne)
            

        Returns :
            (list) : une liste de tuples avec toutes les positions concernées par le périmètre
        """
        pass

    #def presence_fantome(plat, liste_pos):   #A tester
    #    """ Trouve la position des fantomes dans la zone
    #    
    #    Returns :
    #        (list): la liste des positions des fantomes. None s'il n'y en a apas
    #    """
    #    pos_fantomes = []
        for pos in liste_pos :
            if plat['plateau'][pos]['fantome'] != set() :
                pos_fantomes.append(pos)
        if len(pos_fantomes) != 0 :
            return pos_fantomes
        else :
            return None


    #def presence_pacman(plat, liste_pos):    #A tester
    #    """ Trouve la position des pacmans dans la zone
    #    
    #    Returns :
    #        (list): la liste des positions des pacmans. None s'il n'y en a pas
    #    """
        pos_pacmans = []
    #    for pos in liste_pos :
    #        if plat['plateau'][pos]['pacman'] != set() :
                pos_pacmans.append(pos)
        if len(pos_pacmans) != 0 :
            return pos_pacmans
        else :
            return None
#
#
    #def plus_proche(plat, item, fantomes, pacmans, joueur):
    #    """ Compare qui est le plus proche de l'item convoité

        Args():
            plat(dict) : le plateau de jeu
            item(tuple) : la position (ligne, colonne) de l'item
            fantomes(list) : la liste des positions des fantomes présent dans la zone
            joueur(tuple) : position du joueur concerné
#
    #    Returns :
    #        (str) : 
    #    """#
    
    def objet_le_plus_interessant(plat, liste_pos):    #A tester + changer la fonction si on considère que les VITAMINES ne sont pas intéressantes
        """ Trouve l'objet le plus intéressant dans la zone définie
        
        Args():

            plat(dict): le plateau sous forme de dictionnaire
            liste_pos(list): la liste de toutes les positions concernées par la zone
        
        Returns:
            (tuple) : la position de l'objet le plus intéressant le plus près
        """
        priorite = None
        for pos in liste_pos :
            item = plat['plateau'][pos]['objet']
            if item != '':
                if item == const.VALEUR and priorite_item != item :
                    priorite = pos
                    priorite_item = item
                elif item == const.GLOUTON and priorite_item != item :
                    priorite = pos
                    priorite_item = item
                elif item == const.PASSEMURAILLE and priorite_item != item :
                    priorite = pos
                    priorite_item = item
                elif item == const.TELEPORTATION and priorite_item != item :
                    priorite = pos
                    priorite_item = item
                elif item == const.IMMOBILITE and priorite_item != item :
                    priorite = pos
                    priorite_item = item
                else :
                    priorite = pos
                    priorite_item = item
        return priorite



        def direction_pacman():   #décision finale
            pass
            #
    



    # IA complètement aléatoire
    dir_p=  random.choice("NESO")
    dir_f=  random.choice("NESO")
    return dir_p+dir_f          

if __name__=="__main__":
    parser = argparse.ArgumentParser()  
    parser.add_argument("--equipe", dest="nom_equipe", help="nom de l'équipe", type=str, default='Non fournie')
    parser.add_argument("--serveur", dest="serveur", help="serveur de jeu", type=str, default='localhost')
    parser.add_argument("--port", dest="port", help="port de connexion", type=int, default=1111)
    
    args = parser.parse_args()
    le_client=client.ClientCyber()
    le_client.creer_socket(args.serveur,args.port)
    le_client.enregistrement(args.nom_equipe,"joueur")
    ok=True
    while ok:
        ok,id_joueur,le_jeu=le_client.prochaine_commande()
        if ok:
            carac_jeu,le_plateau,les_joueurs=le_jeu.split("--------------------\n")
            actions_joueur=mon_IA(id_joueur,carac_jeu,le_plateau,les_joueurs[:-1])
            le_client.envoyer_commande_client(actions_joueur)
            # le_client.afficher_msg("sa reponse  envoyée "+str(id_joueur)+args.nom_equipe)
    le_client.afficher_msg("terminé")



#Try pacmans

analyse = plateau.analyse_plateau #()
analyse['objets']
analyse['fantomes']
analyse['pacmans']

#On définit un paramètre des alentours qui nous permet d'avoir une vue d'ensemble sur quoi faire


#on sélectionne l'objet le plus proche et le plus int
    #        pos_depart(tuple): la position du joueur (ligne, colonne)
     #       plat(dict): le plateau sous form de dictionnaire
#éressant (points)

#if analyse['objets'][0] < plateau.analyse_plateau #(distance fantome le plus proche / objet voulu)
    #si on est plus proche de l'objet que le fantome, on y va



    #sinon on recherche un nouvel objet à manger dans notre périmètre

plateau.directions_possibles(...)

#on fait exprès de faire 2~3 faux mouvements sur les 4 autorisés : en cas de danger imminent on peut faire un faux mouvement et être téléporté ou si aucun objets ne sont proches






""" Priorité PACMANS :

            pos_depart(tuple): la position du joueur (ligne, colonne)
            plat(dict): le plateau sous form de dictionnaire

1. OBJETS :
- Cerise (&)
- Passemuraille (~)
- Glouton ($)
- Teleportation (!)
- Immobilite (@)
- Vitamine (.)

- Si plus d'items dans la zone définie (sauf VITAMINE) : on se déplace et rammasse les VITAMINES aux alentours ce qui permet de changer de zone
- Si plus d'objets dans la zone définie (y compris VITAMINE) : on se TP en passant le compteur de faux movements à 0

2. DISTANCES :
- None => on s'éloigne lorsque un fantôme rentre dans la zone 'safe' qu'on définiera sauf si items dans la zone où on peut atteindre la case avant le fantôme
- Si Glouton => on arrête d'éviter les fantômes dans la zone
- Si un objet a été privilégié et que 


Priorité FANTÔMES :

1. OBJETS :
- Cerise (&)
- Passemuraille (~)
- Glouton ($)
- Teleportation (!)
- Immobilite (@)
- Vitamine (.)

- Si un joueur est dans la zone et qu'un objet est proche, on reste à distance proche de l'objet pour empêcher les pacmans d'approcher
2. DISTANCES :
- None => on s'approche des objets à grande valeur de la zone
- Si joueur + Glouton => on sort de la zone partagé avec le joueur et on change de zone
- Si il n'y a plus d'objets autre que VITAMINE : on change de zone (faux mouvements)
- Si un joueur est dans la zone alors, il faut se diriger vers sa position 
-Prendre le plus court chemin vers le pacman 

"""


#Ia des fantômes
def pacman_plus_proche(plateau,zone,position_depart,direction):
    """""
    Retourne la position du pacman le plus proche 
        
    Args:
            position_depart(tuple): la position du joueur (ligne, colonne)
            plateau(dict): le plateau sous form de dictionnaire
            valeur: valeur de la zone autour du fantôme

    Returns :
            (tuple): position_pacman
    
    """""
    liste_analyse_plateau = list()
    str_direction_possibles = plateau.directions_possibles(plateau,position_depart,passemuraille=False)
    for direct in str_direction_possibles:
        ana_plateau = plateau.analyse_plateau(plateau, position_depart, direct, len(zone) // 2)
        liste_analyse_plateau.append(ana_plateau)
        print(liste_analyse_plateau)



    #liste_coord_pacman_zone = presence_pacman(zone)
    #nb_lignes_zone = plateau.get_nb_lignes(plateau)
    #nb_colonnes_zone = plateau.get_nb_colonnes(plateau)    
    #distance_mini = None
 #
    #(xB,yB) = position_depart
    #for (x,y) in zone :
    #    if distance_mini is not None or distance_mini < ((xB - x)**2 + (yB + y)**2)*0.5 :
    #        distance_mini = ((xB - x)**2 + (yB + y)**2)*0.5

