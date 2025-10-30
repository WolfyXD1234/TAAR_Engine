#Time As A Resource Engine


#imports
import random


#create all needed stuff to start a battle
combatantDict = {}


#define action class
def baseEffect(stat):
    return(stat-5)

class Action:
    def __init__(self, shell, time):
        self.shell = shell
        self.time = time
    
    def __str__(self):
        return f"{self.shell}\n{self.time}"


#define combatant class
class Combatant:
    def __init__(self, stats, actions, inventory, equipment, traits, time, team):
        self.stats = stats
        self.actions = actions
        self.inventory = inventory
        self.equipment = equipment
        self.traits = traits
        self.time = time
        self.team = team

    def __str__(self):
        return f"{self.stats}\t{self.actions}\t{self.inventory}\t{self.equipment}\t{self.traits}\t{self.time}\t{self.team}"


def createCombatant(name = len(combatantDict), team = -1, delay = 0, stats = {"MaxHP":10, "HP":10}, actions = {"punch": [[[["target","stats", "HP"], baseEffect]], 1]}, inventory = {}, equipment = {}, traits = {}):
    if name not in combatantDict:
        for action in actions:
            actions[action] = Action(actions[action][0], actions[action][1])
        combatantDict[name] = Combatant(stats, actions, inventory, equipment, traits, delay, team)
    else:
        print("combatant not created, name already exists")


#print a list of all combatants
def listAllCombatants(combatantDef = False):
    if combatantDef == False:
        for combatant in combatantDict:
            print(combatant)
    elif combatantDef == True:
        for combatant in combatantDict.items():
            print(combatant[0], end=" : ")
            print(combatant[1].actions)
