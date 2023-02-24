from .storyAgent import storyAgent

class Narrator(storyAgent):
    """ Class permettant d'interragir avec le joueur.
    class attributs: allowed roles with their translation
    attributs: none
    methods: tell, choose_character, player_customization
    """

    roles = {
        "guerrier" : "warrior",
        "archer" : "archer",
        "magicien" : "wizzard"
    }

    def __init__(self):
        pass

    def tell(self, story):
        """Fonction pour afficher les phrases avec transitions"""
        if not isinstance(story, list):
            raise ValueError("Method tell of narrator class expects a list as argument")
        for sentence in story:
            self.transition(3)
            print(sentence)

    def choose_character(self):
        """Fonction pour choisir un  type de personnage
        """
        self.transition(7)
        print("""Avant de commencer ton aventure, qui veux tu incarner ?
- Un guerrier fort et solide comme la pierre
- Un archer agile et souple comme le vent
- Un magicien intelligent et rusé comme le corbeau""")
        while True:
            try:
                player_choice = input('Je veux incarner un : ').lower()
                # Check if player_choice is in the roles class attribut
                player_class = Narrator.roles[player_choice]
                break
            except:
                print('Qui est-ce ? Je ne reconnais pas ce personnage')
        return player_class

    def player_customization(self, player):
        """Fonction permettant de choisir le nom du personnage"""
        self.transition(2)
        name = input("Quel est ton nom aventurier ? : ")
        player.name = name