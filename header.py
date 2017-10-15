from tinydb import Query, TinyDB

MAPS_PATH = "maps/%s"

LEVELS_PARAMETERS = {
    "chasm": {
        "rooms_multiplier": 1,
        "monsters_multiplier": 1,
        "monsters": [""]
    },
    "2": {
        "rooms_multiplier": 1.50,
        "monsters_multiplier": 1.5,
        "monsters": [""]
    },
    "3": {
        "rooms_multiplier": 2,
        "monsters_multiplier": 2.5,
        "monsters": [""]
    }
}


DEFAULT_COUNT_ROOMS = 10

UNIFICATE_MAP_NOTATION = ['B', 'С', 'E']
"""
B - Barrel
C - Chest
E - Enemy
"""
