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
    print('Use Up, Down, Left, Right to move')
    print('Type your cmmands to them')
    print('Use "look" to inspect')
    
    print("     __Advice__:")
    
    print("- Don't forget your commands... It's dangerous to go alone")
    
    title_screen_select()
    