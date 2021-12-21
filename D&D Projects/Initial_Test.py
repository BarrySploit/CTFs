import random


#get input from user on ability scores
str_score = input('What is your Strength ability score? ex: 10 \n')
dex_score = input('What is your Dexterity ability score? ex: 10 \n')
con_score = input('What is your Constitution ability score? ex: 10 \n')
int_score = input('What is your Intelligence ability score? ex: 10 \n')
wis_score = input('What is your Wisdom ability score? ex: 10 \n')
cha_score = input('What is your Charisma ability score? ex: 10 \n')

#document the ability modifiers for the associated ability scores
class AbilityMod:
    strength = int((int(str_score) -10)/2)
    dexterity = int((int(dex_score)-10)/2)
    constitution = int((int(con_score)-10)/2)
    intelligence = int((int(int_score)-10)/2)
    wisdom = int((int(wis_score)-10)/2)
    charisma = int((int(cha_score)-10)/2)

#create function for rolling dice
def rolldice():
    ask = input('What do you want to roll? ex: 2d20')
    final = []
    total = 0
    result = ask.split('d')
    print(result)
    number = int(result[0])
    sides = int(result[1])
    for n in range(0, number):
        final.append(random.randint(1, sides))
    for n in final:
        total += n
    print('You rolled ' + str(final) + ' .')
    print('Your total is ' + str(total) + ' .' )


def str_check():
    result = random.randint(1,20) + AbilityMod.strength
    print(result)

def dex_check():
    result = random.randint(1,20) + AbilityMod.dexterity
    print(result)

def con_check():
    result = random.randint(1,20) + AbilityMod.constitution
    print(result)

def int_check():
    result = random.randint(1,20) + AbilityMod.intelligence
    print(result)


print(AbilityMod.intelligence)
