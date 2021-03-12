import random
import modules.console as console
import modules.bot_code as bot_code # we can put our bot functions in here and reference them with bot_code.function_name()
from colorama import init, Fore
init(autoreset = True) #Set autoreset to True else style configurations would be forwarded to the next print statement

console.clear() # clear the sceen
console.clear_temp_data(["data/all_users.txt"]) # wipe the list of all users

users_text = []
bots = console.load_bot_users() # load up all the bot users from file
bot_padding = max(len(e) for e in bots)+8
insults = console.load_bot_posts() # load up all the insults from file

# here is the chatroom welcome screen
print("Hi, welcome to my nice frienly chat room. Its a safe space.")
name = input(f"Whats your user name? {Fore.GREEN}") # get the users name
all_users = console.load_bot_users() # create the list of all users (bots and new user)
all_users.append(name)
console.save_all_users(all_users) # save this to a file

print(f"{Fore.WHITE}")
print(f"~"*100)
print(f"Welcome to the chatroom {Fore.GREEN}{name}{Fore.WHITE}, please follow the chat rules and remember to have fun. ")
print("~"*100)
print(f"There are currently {Fore.BLUE}{random.randint(17,35)}{Fore.WHITE} people in the chatroom.")
print("")

    # "(ノಠ益ಠ)ノ彡┻━┻"]

wait = 0
while True:
    # print("(ノಠ益ಠ)ノ彡┻━┻")
    # build the user prompts
    bot_prompt = f"{Fore.GREEN}{random.choice(bots).title()}:> " # using colorama.Fore function to colour the text
    user_prompt = f"{Fore.GREEN}{name.title()}:> " # using colorama.Fore function to colour the text

    # user does input
    user_input = input(f"{user_prompt.rjust(bot_padding)}{Fore.WHITE}") # get user input, and justify the text
    users_text.append(user_input)
    console.log_user_post(user_input)

    user_keyword = bot_code.parse_keywords(name, user_input, bot_padding)

    # bot replies
    bot_selection = random.choice(insults)
    bot_selection = bot_selection.replace("user_name", name)
    print(f"{bot_prompt.rjust(bot_padding)}{Fore.WHITE}{bot_selection}") # start printing some bot responses

    bot_code.check_names(name, user_input, bot_padding, all_users)

    # after a few rounds (wait variable) occasional bot repeating user input
    if wait >= 10: # after to rounds start adding the occasional bot repeating user input
        if random.randint(1, 7) == 1:
            users_text = console.load_user_log()
            print(f"{bot_prompt.rjust(bot_padding)}{Fore.WHITE}{random.choice(users_text).capitalize()}")
    wait += 1

    # random flame wars
    if random.randint(1, 15) > 2:
        bot_code.check_names(random.choice(bots), random.choice(bots), bot_padding, all_users)
