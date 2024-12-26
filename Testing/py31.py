import os 
os.system('cls')

class Hero:
    data = []
    
    def __init__(self,name:str,hp:int,mp:int,atk:int,defense:int,classes:str):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.classes = classes
    
    def show_info(self):
        print(8 * '=',' Hero Info ',8 * '=')
        print('Name:',self.name)
        print('HP:',self.hp)
        print('MP:',self.mp)
        print('ATK:',self.atk)
        print('DEFENSE:',self.defense)
        print('CLASSES:',self.classes)
        print(20 * '=')
        
    def add_hero(self):
        print(8 * '=',' Add Hero ',8 * '=')
        name = input('Name: ')
        hp = int(input('HP: '))
        mp = int(input('MP: '))
        atk = int(input('ATK: '))
        defense = int(input('DEFENSE: '))
        classes = input('CLASSES: ')
        self.data.append(Hero(name,hp,mp,atk,defense,classes))
        print('Add Hero Success!')
        print(20 * '=')
        
    def delete_hero(self):
        print(8 * '=',' Delete Hero ',8 * '=')
        name = input('Name: ')
        for i in self.data:
            if i.name == name:
                self.data.remove(i)
                print('Delete Success!')
                print(20 * '=')
                break
            else:
                print('Data not found!')
                print(20 * '=')
    
    
    def update_info(self,name:str,hp:int,mp:int,atk:int,defense:int,classes:str):
        print(8 * '=',' Update ',8 * '=')
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense
        self.classes = classes
        print('Update Success!')
        print(20 * '=')
    
    def attack(self,target):
        print(self.name,'is attacking!. tagert is',target.name)
        if target.defense != 0:
            target.defense -= self.atk
            print('Defense:',target.defense)
        elif target.defense == 0:
            target.hp -= self.atk    
            print('HP:',target.hp)
        elif target.hp == 0:
            self.data.remove(target)
            print('Target is dead!')
            print(20 * '=')
        
    
    
            
    



def main():
    while True:
        print(8 * '=',' Welcome ',8 * '=')
        print('1. Add Hero     2. Delete Hero')
        print('3. Update Hero  4. Attack')
        print('5. Show All     6. Exit')
        print(8 * '=',' Choose ',8 * '=')
        
        choose = input('Please input the number: ')
        
        
        
archer = Hero('Archer',100,50,10,5,'Archer')
knight = Hero('Knight',200,20,5,10,'Knight')

archer.show_info()
knight.show_info()
archer.attack(knight)
archer.attack(knight)
archer.attack(knight)
knight.show_info()



# if __name__ == '__main__':
#     # main()
    
