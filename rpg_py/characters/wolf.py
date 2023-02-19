from .character import Character

class Wolf(Character):

    def __init__(self, name = False):
        super().__init__(300, 30, 15, 40, name)