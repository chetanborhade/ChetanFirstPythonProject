from Classes.game import bcolors, Person

magic = [{"name": "Fire" , "cost": "10", "dmg": "100"},
         {"name": "Thunder", "cost": "10", "dmg": "124"},
         {"name": "Blizzard", "cost": "10", "dmg": "100"}]

player = Person(465, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKs!" + bcolors.ENDC)

while running:
    print("==============================")
    player.choose_action()
    choice = input("Choose action:")
    index = int (choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("choose magic:" )) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)




    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())

    if enemy.get_hp() == 0:
        print(blocker.OKGREEN + "You Win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "Your enemy defeated you!" + bcolors.ENDC)
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