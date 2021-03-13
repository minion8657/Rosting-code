import random
from colorama import init, Fore
init(autoreset = True) #Set autoreset to True else style configurations would be forwarded to the next print statement
import modules.console as console

insults = console.load_file_to_list("data/bot_posts.txt")
bots = console.load_file_to_list("data/bot_users.txt")
all_users = console.load_file_to_list("data/all_users.txt")

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

def flame_war(target_name, speaker_name):
    if speaker_name in bots:
        insult = random.choice(console.load_file_to_list("data/targeted_posts.txt"))
        insult = insult.replace("_user_name_", target_name.title())
        return insult

def check_names(speaker_name, text, padding, all_users):
    words = text.split(" ")
    for target_name in words:
        if target_name.lower() in bots:
            insult = flame_war(speaker_name, target_name)
            if insult == None:
                break
            bot_prompt = f"{Fore.GREEN}{target_name.capitalize()}:> "
            print(f"{bot_prompt.rjust(padding)}{Fore.WHITE}{insult}")
            check_names(target_name, insult, padding, all_users)

def parse_keywords(name, input, padding):
    bot_prompt = f"{Fore.GREEN}{name.capitalize()}:> "
    if "!users" in input:
        print(f"{bot_prompt.rjust(padding)}{Fore.RED}{all_users}")

    if "!insults" in input:
        print(f"{bot_prompt.rjust(padding)}{Fore.RED}{insults}")

    happy = ["happy", ":)", ":D", "happy", "lovely"]
    sad = ["sad"]
    angry = ["angry"]
    moods = [happy, sad, angry]
    for mood in moods:
        for word in input:
            if word in mood:
                return mood[0]

def admin_commands(name, match):
    bot_prompt = f"{Fore.GREEN}{name.capitalize()}:> "
    if match == "!users":
        name = name
