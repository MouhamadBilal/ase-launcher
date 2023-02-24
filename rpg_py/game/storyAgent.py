import os
import time

class storyAgent():
    """ Class qui fait appel aux methods d'arena et narrator
    attributs : none
    methods : transition
    """
    def __init__(self):
        pass

    def transition(self, waiting_time):
        """Fonction pour clear l'écran"""
        time.sleep(waiting_time)
        os.system('cls||clear')