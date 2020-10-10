#item lists
from Text_RPG_Food import *
from Text_RPG_Weapon import *
from Text_RPG_Enemy import *



foodDictionary = [Bread, Apple, CornishPasty, SteamedHam, Beans, Cherries, Steak, TinOfBiscuits, BleachBottle]

weaponDictionary = [Fists, TrustyDagger, ShoddyShank, BattleAxe, Lance, Katana, Club]

enemyDictionary = [Mutant, Brute, Skeleton, KnifeGoblin, Ghoul, MutantGuard, ThiccArab]

itemDictionary = foodDictionary + weaponDictionary

if __name__ == "__main__":
    print("This is a module that creates item dictionaries for the game.")
    input("\n\nPress the enter key to exit.")