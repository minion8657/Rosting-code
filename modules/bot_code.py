import random

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
    insult = insult.replace("<$botname$>", random.choice(botnames))
    return insult
