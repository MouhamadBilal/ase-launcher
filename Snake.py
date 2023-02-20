import pygame
import sys
import random

from pygame.math import Vector2

pygame.init()

largefont = pygame.font.SysFont("comicsansms", 80)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)


def pause():
    paused = True

    message_to_screen("Pause", black, -100, size="large")

    message_to_screen(
        "Appuyez sur G pour continuer ou lancer la partie", black, 25)
    pygame.display.update()

    while paused:
        for event in pygame.EVENT.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    paused == False

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        screen.fill(white)
        clock.tick(60)


def text_objects(text, color):
    game_font = pygame.font.init()
    textSurface = game_font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (screen.width / 2), (screen.height / 2)
    screen.blit(textSurf, textRect)


class SNAKE:
    def __init__(self):
        # definition  la position et direction du snake a l'initialisation
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load(
            'image/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'image/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'image/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'image/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load(
            'image/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'image/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'image/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'image/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(
            'image/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'image/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(
            'image/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'image/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'image/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'image/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
# Ajout d'un block lorsque le snake mage une pomme

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()


# creation du rectangle ou sera dessiner le fruit


    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)

# Methode pour placer le fruit de maniere aleatoire
    def randomize(self):
        # position du X
        self.x = random.randint(0, cell_number - 1)
        # position du Y
        self.y = random.randint(0, cell_number - 1)

        # determine la position finale
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        # pour lancer le jeu on viendras modifier  le False en True
        self.play = False
        # Cree les objets de la classe Snake et Fruit
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

# Tout les elements dessines sur le plateau
    def draw_element(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)


if __name__ == '__main__':
    pygame.init()  # pygame.initialisation
    cell_size = 40
    cell_number = 20
    # taille du plateau de jeu
    screen = pygame.display.set_mode(
        (cell_number * cell_size, cell_number * cell_size))

    clock = pygame.time.Clock()
    apple = pygame.image.load('image/apple.png').convert_alpha()
    game_font = pygame.font.Font(None, 25)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    main_game = MAIN()

    while True:
        # Implematation des touches du joueur et de leur effets sur le jeu dans le game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        # Dessine les elements du code et rafraichit les elements en continu
            screen.fill((175, 215, 70))
            main_game.draw_element()
            pygame.display.update()
            # Fixation du framerate a un maximum afin aue tout ordinateur ai la meme vitesse de jeu
            clock.tick(60)
