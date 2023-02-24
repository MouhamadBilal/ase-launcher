import pygame

class SoundManager:
    def __init__(self):
        self.sounds = {
            'tetris':pygame.mixer.Sound("TetrisGame/Tetris.wav"),
            'game_over':pygame.mixer.Sound("TetrisGame/game_over.wav"),
            'start_game':pygame.mixer.Sound("TetrisGame/start_game.wav"),
        }
    
    def play(self, name):
        self.sounds[name].play()