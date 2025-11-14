[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mMxhKicI)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21623089&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 2: Character Abilities Showcase

## 🎯 Project Overview

A simple character system that demonstrates mastery of the following object-oriented programming fundamentals: 
- Inheritance
- Method Overriding
- Polymorphism
- Composition

This project focuses on core OOP concepts without the complexity of a full game system.

## 🏗️ What I Built:
### **Class Structure (7 Classes Total)**
```
Character (base class)
    ↓
Player (inherits from Character)  
    ↓
Warrior, Mage, Rogue, Cleric (inherit from Player)

Weapon (composition - separate class)
```

### ** Stats for Each Class:**

| Class   | Health | Strength | Magic | Special Ability |
|---------|--------|----------|-------|-----------------|
| Warrior | 120    | 15       | 5     | Power Strike    |
| Mage    | 80     | 8        | 20    | Fireball        |
| Rogue   | 90     | 12       | 10    | Sneak Attack    |
| Cleric  | 100    | 10       | 15    | Divine Power    |

## 🎮 Core Functionality

### **All Characters Have:**
- `attack(target)` - Basic attack method
- `take_damage(damage)` - Reduce health
- `display_stats()` - Print character information

### **Players Additionally Have:**
- `character_class` attribute
- `level` attribute
- Enhanced `display_stats()` that shows player info

### **Special Abilities (Each Class):**
- **Warrior**: `power_strike(target)` - High damage attack
- **Mage**: `fireball(target)` - Magic damage attack
- **Rogue**: `sneak_attack(target)` - Critical hit attack
- **Cleric**: `divine_power(target)` -  Higher damage when you have lower health 

### **Weapons (Composition):**
- `Weapon(name, damage_bonus)` - Characters can HAVE weapons
- `display_info()` - Show weapon information

## 🎲 SimpleBattle System (Provided)

A **SimpleBattle** class was provided, and not designed by me. Use it to have battles:

```python
character1 = Class('Name')                     # Creates the first character. Replace "Class" with the class you want.
character2 = Class('Name')                     # Creates the second character. Replace 'Name' with your character's name.
battle = SimpleBattle(character1, character2)  # Initiates the SimpleBattle class with the characters as opponents
battle.fight()                                 # Simulates and prints a simple battle between the characters
```

## 🎨 Bonus Creative Elements
- New Class: **Cleric** inspired by project 1
- Custom special ability "Divine Intervention" for the cleric class
