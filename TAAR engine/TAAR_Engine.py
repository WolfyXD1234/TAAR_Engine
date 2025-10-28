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
    
#function to create a action
def createAction(name = "punch", shell=[[["stats", "HP"], baseEffect]], time = 1):
    name = Action(shell, time)


#define combatant class
class Combatant:
    def __init__(self, stats, actions, inventory, equipment, traits, team):
        self.stats = stats
        self.actions = actions
        self.inventory = inventory
        self.equipment = equipment
        self.traits = traits
        self.team = team

    def __str__(self):
        return f"{self.stats}\t{self.actions}\t{self.inventory}\t{self.equipment}\t{self.traits}\t{self.team}"


#create a combatant and save its name to a list
def createCombatant(name = len(combatantDict), team = -1, stats = {"MaxHP":10, "HP":10}, actions = {"punch": createAction}, inventory = {}, equipment = {}, traits = {}):
    if name not in combatantDict:
        combatantDict[name] = Combatant(stats, actions, inventory, equipment, traits, team)
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
            print(combatant[1])
