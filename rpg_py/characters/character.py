import random

class Character():
    """Classe avec les différente caractéristique des personnages
    class attribut: actions
    attributs: name, life, attack, defense, agility
    methods: attacks, escape
    """
    actions = {
        'a': 'attaquer',
        'f': 'fuir'
    }

    def __init__(self, life, attack, defense, agility, name = False):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def attacks(self, target):
        """Fonction qui fait attaquer et qui infflige des dégât si non évité
        """
        print("{} attaque violemment {}".format(self.name, target.name))
        # Offre une chance d'éviter l'attaque (dépend de l'agilité)
        if random.randrange(0,100) <= target.agility:
            print("{} a esquivé l'attaque".format(target.name))
            return False
        target.life -= self.attack - (target.defense/5)
        # Vérifie que la santé peut tomber jusqu'à 0
        if target.life < 0:
            target.life = 0
        print("{} a maintenant {} de vie".format(target.name, target.life))

    def escape(self):
        """Fonction qui permet de s'échapper et de mettre fin au combat"""
        # Faible chance de s'échapper selon l'agilité
        agi = round(self.agility/5)
        if random.randrange(0,100) <= agi:
            return True
        return False

    def make_action(self, action, ennemy):
        """Fonction qui execute la methode requise pour chaque actions"""
        if action not in self.actions:
            print('Action impossible')
            return False
        if action == 'a':
            self.attacks(ennemy)
        elif action == 'f':
            if self.escape():
                # Si le personnage arrive à s'enfuir c'est la fin du combat
                print("Vous réussissez à fuir au dernier moment dans un élan d'agilité")
                raise Exception('Character Escaping')
            else:
                print('Votre ennemi vous rattrape !')
        elif action == 's':
            self.heal()
        return True

    def __str__(self):
        return "{} : vie = {}".format(self.name, self.life)