from game.narrator import Narrator
from game.factory import Factory
from game.arena import Arena

if __name__ == '__main__':
    # Demarrage de l'histoire
    narrator = Narrator()
    # Demarrage du combat
    arena = Arena()

    introduction = [
        "Bienvenue aventurier aux portes d'un nouveau monde de magie et de légendes.",
        "Ici commence ton histoire, laisse toi guider par le narrateur de ce monde.",
        "Ta légende raisonnera pour des siècles et des siècles"
    ]
    narrator.tell(introduction)
    # Choix du type de personnage dans Factory
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)
    # Selection de l'ennemi dans Factory
    ennemy = Factory.get_character('orc')
    ennemy.name = 'Gentro'

    # Histoire racontée
    story = [
        'Votre voyage commence. Vous entrez dans le temple des anciens',
        'Il fait froid, et la grande salle principale est vide',
        'Vous entendez alors un bruit sourd, vous vous retournez',
        'Les portes se referment derrière vous',
        'Vous vous rendez compte que vous êtes plus seul(e)',
        'Un Orc surgit et commence à vous attaquer ',
    ]
    narrator.tell(story)

    # Début du combat
    arena.fighters_enter(player, ennemy)
    arena.battle()
    
   # possibilité de developper l'histoire
