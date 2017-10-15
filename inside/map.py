import numpy as np

import header as h
import inside


class Map:
    def __init__(self, act_name):
        self.count_of_rooms = h.DEFAULT_COUNT_ROOMS * \
            h.LEVELS_PARAMETERS[act_name]["rooms_multiplier"]

        self.map = inside.gen.construct_map(
            self.count_of_rooms, h.LEVELS_PARAMETERS[act_name]["monsters_multiplier"])

        self.danger_coeff_rooms = self.count_of_rooms / self.map["count_of_enemies"]

    def get_point_map
