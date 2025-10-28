import TAAR_Engine
import random

def minusOne(stat):
    return stat-1

TAAR_Engine.createCombatant("bobert", 1, {"MaxHP":10, "HP":10}, {"Upunch": TAAR_Engine.createAction("Upunch", [[["stats", "HP"], minusOne],[["stats", "MaxHP"], minusOne]], 1)})

TAAR_Engine.listAllCombatants(True)