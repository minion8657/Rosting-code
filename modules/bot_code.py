import random
from colorama import init, Fore
init(autoreset = True) #Set autoreset to True else style configurations would be forwarded to the next print statement
import modules.console as console

insults = console.load_bot_posts()
bots = console.load_bot_users()
all_users = console.load_all_users()

def get_targeted_insult(botnames, targeted):
    """ Constructs a random insult from a list of bot names and a list of insults.
        Selects a random insult from the list, looks for the characters <$botname$>,
        and replaces it with a random selection from the list of bot names.
    Arguments:
        a: a list of botnames as strings.
        b: a list of insults as strings.
    Returns:
        The constructed insult as a string.
    """
    insult = random.choice(targeted)
    insult = insult.replace("_user_name_", random.choice(botnames))
    return insult

def flame_war(name):
    insult = random.choice(console.load_targeted_posts())
    insult = insult.replace("_user_name_", name)
    return insult

def check_names(speaker, text, padding, all_users):
    words = text.split(" ")
    for name in words:
        if name.lower() in bots:
            insult = flame_war(speaker)
            bot_prompt = f"{Fore.GREEN}{name.capitalize()}:> "
            print(f"{bot_prompt.rjust(padding)}{Fore.WHITE}{insult}")
            check_names(name, insult, padding, all_users)

def parse_keywords(input):
    happy = ["happy", ":)", ":D", "happy", "lovely"]
    sad = ["sad"]
    angry = ["angry"]
    moods = [happy, sad, angry]
    for mood in moods:
        for word in input:
            if word in mood:
                return mood[0]
