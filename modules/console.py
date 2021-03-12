# this module contains classes, functions and variables used globally by the system to operate and display the console output.
from os import system, name

def clear():
    """ Checks to see if this is Linux/MacOS or WinNT, then uses the correct function to clear the screen.
    Arguments:
        None
    Returns:
        None
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def load_system_config():
    """ Loads saved config settings from a file. Accepts no arguments. Returns a dictionary.
    """
    with open("data/system_config.txt.txt") as file:
        config = [line.rstrip('\n') for line in file]
    return config

def save_system_config():
    x = 0

def load_current_users():
    with open("data/current_users.txt") as file:
        bots = [line.rstrip('\n') for line in file]
    return bots

def load_bot_posts():
    with open("data/bot_posts.txt") as file:
        insults = [line.rstrip('\n') for line in file]
    return insults

def load_targeted_posts():
    with open("data/targeted_posts.txt") as file:
        insults = [line.rstrip('\n') for line in file]
    return insults

def log_user_post(post):
    """ Appends user input to a text file
        Argument is the users input as a string. Nothing is returned.
    """
    with open("data/user_posts.txt", "a") as file:
        file.write(post + "\n")

def load_user_log():
    """ Reads user input from a text file into a list.
        No arguments. Returns users logged posts as a list object.
    """
    with open("data/user_posts.txt") as file:
        posts = [line.rstrip('\n') for line in file]
    return posts
