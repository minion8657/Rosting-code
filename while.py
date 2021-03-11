import random

# insults = ["Thats a lame sentence.", "That was a crappy sentence.", "Wow, you should get some English lessons."]
def random_insult():
    global bots
    insults = [f"Die {random.choice(bots).capitalize()}", f"Oi, {random.choice(bots).capitalize()}. Why don't you get lost"]
    return random.choice(insults)

users_text = []
bots = ["bob", "jeff", "zaphod", "quark_killa", "alex", "stuart", "felix", "your dad", "Lily", "I'm a bot"]

print("Hi, welcome to my nice frienly chat room. Its a safe space.")
name = input("Whats your user name? ")
insults = [random_insult(), "Wow, you're so lame", "Who's this stupid guy?", f"Nice to meet you {name.capitalize()}", "You’re the reason God created the middle finger", "You’re a grey sprinkle on a rainbow cupcake", "Light travels faster than sound, which is why you seemed bright until you spoke", "I’ll never forget the first time we met. But I’ll keep trying"]
print("")
wait = 0

while True:
    users_text.append(input(f"{name.capitalize()}:> "))
    print(f"{random.choice(bots).capitalize()}:> {random.choice(insults)}")
    if wait >= 10:
        if random.randint(1, 7) == 1:
            print(f"{random.choice(bots).capitalize()}:> {random.choice(users_text).capitalize()}")
    wait += 1




# while x < 10:
#     print(x)
#     print("This isn't 10 yet")
#     x = x + 1
#
#
# print(f"x is now {x}")
#
# Hi=9
#
# while Hi > 2:
#     print(Hi)
#     print("This is bigger than 2")
#     Hi=Hi-1
# print(f"Hi is now {Hi}")
# print("Hi is now Weak")
# print(f"The cube of {Hi} is {Hi**3}")
# print(f"We calculated the cube of x in a print sting but the value of x is still {Hi}")
