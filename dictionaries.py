#item lists
from Text_RPG_Food import *
from Text_RPG_Weapon import *
from Text_RPG_Enemy import *
from Text_RPG_Armour import *

foodDictionary = [Bread, Apple, CornishPasty, SteamedHam, Beans, Cherries, Steak, TinOfBiscuits, BleachBottle, CheeseSandwich, FullEnglishBreakfast, LambShank, FishAndChips, Olives, SausageRoll]

weaponDictionary = [Fists, TrustyDagger, ShoddyShank, BattleAxe, Lance, Katana, Club, BroadSword, StilettoKnife, SteelAxe, SilverSabre, MagnesiumKnife, AluminiumMallet, IronCutlass, RubySpear, ThrowingKnife, TitaniumAxe, Mace]

enemyDictionary = [Mutant, Brute, Skeleton, KnifeGoblin, Ghoul, MutantGuard, ThiccArab, DarkKnight, Drunk, Knight, Giant, Looter, Samurai, Goblin, PoisonousSpider, Hound, WildBoar, Hunter, MutantWarrior, HostileTrader, BruteGuard, Primitive, PrimitiveLeader, PrimitiveSlave, PrimitiveGuard]

armourDictionary = [ClothArmour, LeatherArmour, ChainArmour, PlateArmour, HeavyPlateArmour]

itemDictionary = foodDictionary + weaponDictionary + armourDictionary

grocerBaseItems = [Bread, CheeseSandwich]

blacksmithBaseItems = [TrustyDagger, BroadSword]

foodBlacklist = [Cherries, Beans]

if __name__ == "__main__":
    print("This is a module that creates item dictionaries for the game.")
    input("\n\nPress the enter key to exit.")