import random
from time import sleep

class Human:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.attack_strength = 20
    
    def take_damage(self, damage: int):
        self.health -= damage
    
    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.__class__.__name__}!")
        enemy.take_damage(self.attack_strength)
    
    def heal(self):
        self.health += random.randint(1, 50)
    
    def increase_strength(self):
        self.attack_strength += random.randint(1, 10)

class Enemy:
    def __init__(self, health: int, attack_strength: int):
        self.health = health
        self.attack_strength = attack_strength
    
    def take_damage(self, damage: int):
        self.health -= damage
    
    def attack(self, human: Human):
        print(f"{self.__class__.__name__} attacks {human.name}!")
        human.take_damage(self.attack_strength)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(health=150, attack_strength=30)

class Elf(Enemy):
    def __init__(self):
        super().__init__(health=120, attack_strength=25)

class Gnome(Enemy):
    def __init__(self):
        super().__init__(health=80, attack_strength=15)

class Game:
    def __init__(self):
        self.level = 1
    
    def fight(self, human: Human, enemy) -> bool:
        while human.health > 0 and enemy.health > 0:
            human.attack(enemy)
            if enemy.health > 0:
                enemy.attack(human)
            print(f"{human.name}'s health: {human.health} - {enemy.__class__.__name__}'s health: {enemy.health}")
        if human.health <= 0:
            print(f"{human.name} has been defeated!")
            return False
        else:
            print(f"{human.name} defeated the {enemy.__class__.__name__}!")
            human.heal()
            human.increase_strength()
            return True
    
    def play(self):
        name = input("Enter your warrior name: ")
        human = Human(name)
        
        while self.level <= 15:
            print(f"\n=== Level {self.level} ===")
            if self.level == 1:
                print(f"{human.name}'s health: {human.health}")
                enemy = Gnome()
                print(f"A wild {enemy.__class__.__name__} appears!")
                result = self.fight(human, enemy)
            
                if result:
                    self.level += 1
                    print(f"Congratulations! You have advanced to level {self.level}")
                    sleep(5)
                else:
                    print("Game Over!")
                    sleep(5)
                    break
            else:       
                print(f"{human.name}'s health: {human.health}")
                enemy_type = random.choice([Ogre, Elf, Gnome])
                enemy = enemy_type()
                print(f"A wild {enemy.__class__.__name__} appears!")
                result = self.fight(human, enemy)
                
                if result:
                    self.level += 1
                    print(f"Congratulations! You have advanced to level {self.level}")
                    sleep(5)
                else:
                    print("Game Over!")
                    sleep(5)
                    break
        else:
            print("Congratulations! You have won the game!")
        

# Start the game
game = Game()
game.play()
