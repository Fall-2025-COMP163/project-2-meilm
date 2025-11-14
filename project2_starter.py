'''
COMP 163 - Project 2: Character Abilities Showcase
Name: Isaac Manson
Date: 14 November 2025

AI Usage: Perplexity
    - Generated basic aspects of the code (print functions, f-strings, constructors)
    - Used the equations I made to generate the code for the character's attacks and special abilities
    - Reminded me how super() worked, it's syntax, and when it should be called
    - Reminded me how composition works, and how it differs from inheritance
'''

import random
import math
# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================
class SimpleBattle:
    '''
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    '''
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        '''Simulates a simple battle between two characters'''
        print(f'\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===')
        
        # Show starting stats
        print('\nStarting Stats:')
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f'\n--- Round 1 ---')
        print(f'{self.char1.name} attacks:')
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f'\n{self.char2.name} attacks:')
            self.char2.attack(self.char1)
        
        print(f'\n--- Battle Results ---')
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f'🏆 {self.char1.name} wins!')
        elif self.char2.health > self.char1.health:
            print(f'🏆 {self.char2.name} wins!')
        else:
            print('🤝 It\'s a tie!')

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    '''Base class for all characters.'''
    
    def __init__(self, name, health, strength, magic):
        self.name, self.health, self.strength, self.magic = name, health, strength, magic
        
    def attack(self, target, calculation='strength'):
        '''
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        '''
        if calculation == 'strength':
            damage = self.strength
        else: damage = int(calculation)

        target.take_damage(damage) 
        print(f'{self.name} attacks {target.name} for {damage} damage.')
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        
    def display_stats(self): 
        print(f'{'Name:':<10}{self.name}') 
        print(f'{'Health:':<10}{self.health}')
        print(f'{'Strength:':<10}{self.strength}')
        print(f'{'Magic:':<10}{self.magic}')

class Player(Character):
    '''Base class for player characters.'''
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class

    def display_stats(self):
        super().display_stats()
        print(f'{self.name} is a {self.character_class}.')

class Warrior(Player):
    '''Warrior class - strong physical fighter.'''
    def __init__(self, name):
        '''Warriors have: high health, high strength, low magic'''
        super().__init__(name, 'Warrior', 120, 15, 5)

    def attack(self, target):
        '''
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        '''
        calculation = self.strength + 5
        super().attack(target, calculation)

    def power_strike(self, target):
        '''Special warrior ability - a powerful attack that does extra damage.'''
        calculation = self.strength + 10
        super().attack(target, calculation)

class Mage(Player):
    '''Mage class - magical spellcaster.'''
    def __init__(self, name):
        '''Mages have: low health, low strength, high magic'''
        super().__init__(name, 'Mage', 80, 8, 20)
 
    def attack(self, target):
        '''
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        '''
        calculation = self.magic
        super().attack(target, calculation)
  
    def fireball(self, target):
        '''Special mage ability - a powerful magical attack.'''
        calculation = self.magic + 5
        super().attack(target, calculation)

class Rogue(Player):
    '''Rogue class - quick and sneaky fighter.'''
    def __init__(self, name):
        '''Rogues have: medium health, medium strength, medium magic'''
        super().__init__(name, 'Rogue', 90, 12, 10)
  
    def attack(self, target):
        '''
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        '''
        if random.randint <= 3:
            calculation = self.strength * 2
            print('A critical hit!')
        else: self.strength = self.strength
        super().attack(target, calculation)   

    def sneak_attack(self, target):
        '''Special rogue ability - guaranteed critical hit.'''
        calculation = self.strength * 2
        super().attack(target, calculation)

class Cleric(Player):
    '''Cleric class - holy magician'''
    def __init__(self, name):
        '''Clerics have: high health, medium strength, high magic'''
        super().__init__(name, 'Cleric', 100, 10, 15)

    def attack(self, target):
        # Every attack has a chance to be from the cleric (strength) or the cleric's diety (magic)
        if random.randint(1,3) == 3:
            calculation = self.magic
        else: calculation = self.strength
        super().attack(target, calculation)

    def divine_power(self, target):
        '''this attack gets stronger as the cleric's HP gets lower'''      
        calculation = math.ceil(500 / (self.health + 5))
        super().attack(target, calculation)

class Weapon:
    '''
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    '''
    
    def __init__(self, name, damage_bonus):
        self.name, self.damage_bonus = name, damage_bonus

    def display_info(self): 
        print(f'{'Name:':<14}{self.name}')
        print(f'{'Damage Bonus:':<14}{self.damage_bonus}')

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == '__main__':
    print('=== CHARACTER ABILITIES SHOWCASE ===')
    print('Testing inheritance, polymorphism, and method overriding')
    print('=' * 50)
'''
    # TODO: Create one of each character type
    # warrior = Warrior('Sir Galahad')
    class
    # mage = Mage('Merlin')
    # rogue = Rogue('Robin Hood')
    
    # TODO: Display their stats
    # print('\n📊 Character Stats:')
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print('\n⚔️ Testing Polymorphism (same attack method, different behavior):')
    # dummy_target = Character('Target Dummy', 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f'\n{character.name} attacks the dummy:')
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print('\n✨ Testing Special Abilities:')
    # target1 = Character('Enemy1', 50, 0, 0)
    # target2 = Character('Enemy2', 50, 0, 0)
    # target3 = Character('Enemy3', 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print('\n🗡️ Testing Weapon Composition:')
    # sword = Weapon('Iron Sword', 10)
    # staff = Weapon('Magic Staff', 15)
    # dagger = Weapon('Steel Dagger', 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print('\n⚔️ Testing Battle System:')
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print('\n✅ Testing complete!')'''