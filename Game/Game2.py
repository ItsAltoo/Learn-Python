import os
os.system('cls')

class Hero:
    
    def __init__(self,name,health,power,armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        
    def attack(self, enemy):
        print(self.name , ' Menyerang ' , enemy.name,",darah :",enemy.health)
        enemy.getAttack(self,self.power)
        
    def getAttack(self,enemy,enemyPower):
        print(self.name, 'diserang', enemy.name)
        attacked = enemyPower
        print('Get attack :' + str(attacked))
        self.health -= attacked
        print('darah ' + self.name + " tersisa " + str(self.health))
        
sniper = Hero('sniper',100,25,50)
tank = Hero('tanker',200,10,50)

sniper.attack(tank)
print('\n')
tank.attack(sniper)
print('\n')
sniper.attack(tank)
print('\n')
tank.attack(sniper)
print('\n')
sniper.attack(tank)
print('\n')
tank.attack(sniper)
print('\n')

