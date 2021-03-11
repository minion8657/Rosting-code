import random

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

print("Hi, welcome to my nice frienly chat room. Its a safe space.")
name = input("Whats your user name? ")
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

while True:
    # print("(ノಠ益ಠ)ノ彡┻━┻")
    users_text.append(input(f"{name.capitalize()}:> "))
    print(f"{random.choice(bots).capitalize()}:> {random.choice(insults)}")
    if wait >= 10:
        if random.randint(1, 7) == 1:
            print(f"{random.choice(bots).capitalize()}:> {random.choice(users_text).capitalize()}")
    wait += 1
