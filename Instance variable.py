import random

class Enemy:

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print(self.atkl)

enemy1 = Enemy(40, 49)
enemy1.getAtk()

enemy2 = Enemy(90, 80)
enemy2.getAtk()



'''

import random

class Enemy:

    def _init_(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

        def getAtk(self):
            print(self.atkl)

enemy1 = Enemy(1, 2)
enemy1.getAtk()


enemy2 = Enemy(3, 4)
enemy2.getAtk()

'''