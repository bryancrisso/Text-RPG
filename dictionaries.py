#item lists
from Text_RPG_Food import *
from Text_RPG_Weapon import *



foodDictionary = [Bread, Apple]

weaponDictionary = [Fists, TrustyDagger, ShoddyShank, BattleAxe]

itemDictionary = foodDictionary + weaponDictionary

if __name__ == "__main__":
    print("This is a module that creates item dictionaries for the game.")
    input("\n\nPress the enter key to exit.")