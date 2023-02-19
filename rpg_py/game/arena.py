from .storyAgent import storyAgent

class Arena(storyAgent):
    """Classe montrant le lieu où se déroule le jeu
    attributs : player, ennemy
    methods: fighters_enter, fighters_leave, battle
    """

    def __init__(self):

        self.player = False
        self.ennemy = False

    def fighters_enter(self, player, ennemy):
        """Fonction pour utiliser les objets player et enemy """
        self.player = player
        self.ennemy = ennemy

    def fighters_leave(self):
        """Fonction pour clear les stats player et enemy"""
        self.player = False
        self.ennemy = False

    def battle(self):
        """fonction pour demander au joueur d'executer une action"""
        self.transition(2)
        # Tant que que les personnage sont en vie
        while self.player.life > 0 and self.ennemy.life > 0:
            try:
                action_is_allowed = False
                # Vérifie si les actions du joueur sont exécutée
                while not action_is_allowed:
                    print("{} || {}".format(self.player, self.ennemy))
                    action = input('Que souhaitez-vous faire {} ? : '.format(self.player.actions)).lower()
                    action_is_allowed = self.player.make_action(action, self.ennemy)
            # Si le personnage arrive à fuir
            except Exception as e:
                break
            # Le tour ennemi, s'il n'est pas mort
            if self.ennemy.life > 0:
                self.ennemy.attacks(self.player)
            self.transition(5)
        # Fin du combat
        print('Le combat prend fin')
        self.fighters_leave()