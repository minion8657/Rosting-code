# this module contains classes, functions and variables used globally by the system to operate and display the console output.
from os import system, name

def clear_screen():
    "Checks to see if this is Linux/MacOS or WinNT, then uses the correct function to clear the screen."
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def clear_temp_data(files=[]):
    "Takes in 1 or more file paths as a list of strings, then clears all data from each file. No return."
    for file in files:
        with open(file, "wt") as file:
            file.seek(0)
            file.truncate()

def load_system_config():
    "Loads saved config settings from a file. Accepts no arguments. Returns a dictionary."
    with open("data/system_config.txt.txt") as file:
        config = [line.rstrip('\n') for line in file]
    return config

def save_system_config():
    x = 0

def load_file_to_list(file):
    with open(file) as file:
        list = [line.rstrip('\n') for line in file]
    return list

def save_all_users(users):
    with open("data/all_users.txt", "wt") as file:
        file.write('\n'.join(users))

def append_to_file(text, file):
    """ Appends text (argument 1) to the a file (argument 2 = filename)
        Argument 1 = text to append, as a string.
        Argument 1 = file to append to, as a string.
        Nothing is returned.
    """
    with open(file, "a") as file:
        file.write(text + "\n")

def log_user_post(post):
    """ Appends user input to a text file
        Argument is the users input as a string. Nothing is returned.
    """
    with open("data/user_posts.txt", "a") as file:
        file.write(post + "\n")
