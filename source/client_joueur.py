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
    ok=TrueGlouton (ac_jeu,le_plateau,les_joueurs[:-1])
            le_client.envoyer_commande_client(actions_joueur)
            # le_client.afficher_msg("sa reponse  envoyée "+str(id_joueur)+args.nom_equipe)
    le_client.afficher_msg("terminé")




#Try pacmans

analyse = plateau.analyse_plateau #()
analyse['objets']
analyse['fantomes']
analyse['pacmans']

#On définit un paramètre des alentours qui nous permet d'avoir une vue d'ensemble sur quoi faire


#on sélectionne l'objet le plus proche et le plus intéressant (points)

if analyse['objets'][0] < plateau.analyse_plateau #(distance fantome le plus proche / objet voulu)
    #si on est plus proche de l'objet que le fantome, on y va



    #sinon on recherche un nouvel objet à manger dans notre périmètre

plateau.directions_possibles(...)

#on fait exprès de faire 2~3 faux mouvements sur les 4 autorisés : en cas de danger imminent on peut faire un faux mouvement et être téléporté ou si aucun objets ne sont proches






""" Priorité PACMANS :

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
- Si un joueur




"""