from Classes.game import bcolors, Person

magic = [{"name": "Fire" , "cost": "10", "dmg": "60"},
         {"name": "Thunder", "cost": "10", "dmg": "60"},
         {"name": "Blizzard", "cost": "10", "dmg": "60"}]

player = Person(465, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK" + bcolors.ENDC)
while running:
    print("========================")
    player.choose_action()
    choice = input("Choose action:")

    print("You chose", choice)


    running = False























'''
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

'''














'''
from classes.game import person, bcolors

magic = [{"name": "fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = person(460, 65, 80, 34, magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

'''