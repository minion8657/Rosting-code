import random
from os import system, name
from colorama import init, Fore
init(autoreset = True) #Set autoreset to True else style configurations would be forwarded to the next print statement
import modules.bot_code as bot_code # we can put our bot functions in here and reference them with bot_code.function_name()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
clear()

# insults = ["Thats a lame sentence.", "That was a crappy sentence.", "Wow, you should get some English lessons."]
def random_insult():
    global bots
    insults = [ f"Die {random.choice(bots).capitalize()}",
                f"Oi, {random.choice(bots).capitalize()}. Why don't you get lost",
                f"Has anyone seen {random.choice(bots).capitalize()}?"]
    return random.choice(insults)

users_text = []
bots = ["bob",
        "jeff",
        "zaphod",
        "quark_killa",
        "alex",
        "stuart",
        "felix",
        "your dad",
        "Lily",
        "I'm a bot",
        "Billy",
        "Layla",
        "Your mum",
        "Glastaff",
        "David camreon",
        "Jerremy Corbyn",
        "Glee"]
bot_padding = max(len(e) for e in bots)+8
print(bot_padding)
print("Hi, welcome to my nice frienly chat room. Its a safe space.")
name = input(f"Whats your user name? {Fore.GREEN}")
print("~"*100)
print(f"Welcome to the chatroom {Fore.GREEN}{name}{Fore.WHITE}, please follow the chat rules and remember to have fun. ")
print("~"*100)
print(f"There are currently {Fore.BLUE}{random.randint(17,35)}{Fore.WHITE} people in the chatroom.")

insults = [ random_insult(),
            "Wow, you're so lame",
            "Who's this stupid guy?",
            f"Nice to meet you {name.capitalize()}",
            "You’re the reason God created the middle finger",
            "You’re a grey sprinkle on a rainbow cupcake",
            "Light travels faster than sound, which is why you seemed bright until you spoke",
            "I’ll never forget the first time we met. But I’ll keep trying",
            "Your face makes onions cry :p",
            "You bring everyone so much joy… when you leave the room",
            "OH MY GOD! IT SPEAKS!",
            "You just might be why the middle finger was invented in the first place",
            "You have miles to go before you reach mediocre",
            "Have you heard of the new species of animals called sheep?",
            "Hi guys how was you're day?",
            "I've been baking cakes who wanst some?",
            "Its, Raining :(",
            "Guess what guys! This chat is getting updated soon!",
            "Nobody cares",
            "Nope",
            "You bring everyone so much joy! You know, when you leave the room. But, still",
            "Lol",
            "Lmao",
            "Ha ha You're so funny!"]


            # "(ノಠ益ಠ)ノ彡┻━┻"]
print("")
wait = 0

# testing the bot_code module
# for i in range(10):
#     print(bot_code.get_targeted_insult(bots, ["Hey <$botname$>, whats up?"]))

while True:
    # print("(ノಠ益ಠ)ノ彡┻━┻")
    bot_prompt = f"{Fore.GREEN}{random.choice(bots).capitalize()}:> " # using colorama.Fore function to colour the text
    user_prompt = f"{Fore.GREEN}{name.capitalize()}:> " # using colorama.Fore function to colour the text

    users_text.append(input(f"{user_prompt.rjust(bot_padding)}{Fore.WHITE}")) # get user input, and justify the text

    print(f"{bot_prompt.rjust(bot_padding)}{Fore.WHITE}{random.choice(insults)}") # start printing some bot responses
    if wait >= 10: # after to rounds start adding the occasional bot repeating user input
        if random.randint(1, 7) == 1:
            print(f"{bot_prompt.rjust(bot_padding)}{Fore.WHITE}{random.choice(users_text).capitalize()}")
    wait += 1
