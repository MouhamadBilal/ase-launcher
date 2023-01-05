import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

# Création du joueur

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.pm = 0
        self.status = []
        self.location = ''
        
myPlayer = player()

# ecran de selection 
def title_screen_select():
    option = input(">")
    if option.lower() == ("play"):
        start_game()
        
    elif option.lower() == ("help"):
        help_menu()
        
    elif option.lower() == ("quit"):
        sys.exit
        
    while option.lower() not in ['play', 'help', 'quit']:
        print('please enter a valid command')
        option = input(">")
        if option.lower() == ("play"):
            start_game()
        
        elif option.lower() == ("help"):
            help_menu()
        
        elif option.lower() == ("quit"):
            sys.exit
            
            
# ecran d'accueil

def title_screen():
    os.system('clear')
    print('##### Welcome to Shell RPG #####')
    print('         - Play -        ')
    print('         - Help -        ')
    print('         - Quit -        ')
    
def help_menu():
    print('##### Welcome to Shell RPG #####')
    print('- Use Up, Down, Left, Right to move')
    print('- Type your cmmands to them')
    print('- Use "look" to inspect')
    
    print("     __Advice__:")
    
    print("- Don't forget your commands... It's dangerous to go alone")
    
    title_screen_select()
    
    # Fonctionnalité in-game
    
    
    # Carte
    
    #|_|_|_|_|
    #|_|_|_|_|
    #|_|_|_|_|
    #|_|_|_|_|
    
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
    
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'
    
solved_place = { 'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False
                }

zonemap = {
    'a1': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    
    
    'a2': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    
    'a3': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    
    'a4': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    
    'b1': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    'b2': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    'b3': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    'b4': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
       
    },
    
    'c1': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    'c2': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    'c3': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    
    'c4': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    
    'd1': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    
    'd2': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    
    'd3': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
    
    'd4': {
       ZONENAME: "",
       DESCRIPTION:'',
       EXAMINATION:'examination',
       SOLVED:False,
       UP: 'up',
       DOWN: 'down',
       LEFT: 'west',
       RIGHT: 'east'
    },
}
    