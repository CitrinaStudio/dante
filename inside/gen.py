import hashlib
import string
import zlib

import numpy as np
from tinydb import Query, TinyDB

import header as h
import inside


def _reg_door(x, y, room_name, door_position):
    db = TinyDB('game.json')

    doors = db.table("doors")

    id = len(doors.all()) + 1

    door_info = {"id": id, "name": room_name, "x": x, "y": y, "door_position": door_position}
    doors.insert(door_info)


def _gen_room(enemy_miltiplier, type="default"):

    room_name = inside.gen.gen_adler32_hash(
        np.random.uniform(-1000, 1000))

    width = np.random.randint(8, 13)
    height = np.random.randint(6, 10)

    doors_in_room = 0

    count_of_enemies = 0

    room = ""

    boss_door = 0

    room += "#" * width + "\n"

    x = y = 1

    for y in range(0, height - 2, 1):

        if np.random.random() > 0.7 and doors_in_room < 4:
            room += "D"
            doors_in_room += 1
            _reg_door(x, y, room_name, "left")
        else:
            room += "#"

        for x in range(0, width - 2, 1):

            map_notation = np.random.choice(h.UNIFICATE_MAP_NOTATION)

            if map_notation == "E" and np.random.random() < (10 * enemy_miltiplier) / (width * height):
                room += map_notation
                count_of_enemies += 1
            elif np.random.random() > (np.random.random() * 10):
                room += "B"

            elif 0.8 > np.random.random() > 0.7:
                room += "C"

            else:
                room += " "

        if np.random.random() > 0.7 and doors_in_room < 4:
            room += "D\n"
            doors_in_room += 1
            _reg_door(x, y, room_name, "right")
        else:
            room += "#\n"

    room += "#" * width + "\n"

    room_strings = room.split("\n")  # Room array

    room_length = len(room_strings)

    del room_strings[room_length - 1]  # Delete empty item

    room_length = len(room_strings)

    for _ in range(0, width):  # Insert doors in walls
        if doors_in_room < 4:
            wall = np.random.choice([0, room_length - 1])  # Wall number

            position = "top" if wall == 0 else "bottom"  # Door position

            wall_lenght = width  # Wall Length

            symbol_num = np.random.randint(1, wall_lenght - 1)  # Symbol number in wall

            room_strings[wall] = room_strings[wall][:symbol_num] + \
                "D" + room_strings[wall][symbol_num + 1:]  # Door inserting

            doors_in_room += 1

            _reg_door(x, y, room_name, position)

        if type == "boss_room" and boss_door == 0:
            wall = np.random.choice([0, room_length - 1])  # Wall number

            position = "top" if wall == 0 else "bottom"  # Door position

            wall_lenght = width  # Wall Length

            symbol_num = np.random.randint(1, wall_lenght - 1)  # Symbol number in wall

            room_strings[wall] = room_strings[wall][:symbol_num] + \
                "I" + room_strings[wall][symbol_num + 1:]  # Boss door inserting

            boss_door = 1

    room_strings.append("")  # Insert empty element for "\n" in array cunt

    room = "\n".join(room_strings)  # Room array to string

    room_file = open(h.MAPS_PATH % room_name, "w")
    room_file.write(room)
    room_file.close()

    return {"room": room, "count_of_enemies": count_of_enemies}


def gen_adler32_hash(params):
    """ Генерация adler32 """

    return str(hex(zlib.adler32(str(params).encode("utf-8"))).split('x')[-1])


def gen_crc32_hash(params):
    """ Генерация crc32 """

    return str(hex(zlib.crc32(str(params).encode("utf-8"))).split('x')[-1])


def gen_md5_hash_file(file_name):
    """ Генерация md5 """

    return hashlib.md5(open(file_name, 'rb', encoding="utf-8").read()).hexdigest()


def gen_name(size):
    """ Генерация строки(имени) """

    return string.capwords(''.join(np.random.choice(
        string.ascii_uppercase + string.digits) for _ in range(size)))


def construct_map(count_of_rooms, enemy_miltiplier):
    rooms = np.array([], dtype=str)

    boss_room = 0

    count_of_enemies = 0

    for _ in range(0, count_of_rooms, 1):

        if boss_room == 0:
            room_params = _gen_room(enemy_miltiplier, type="boss_room")
            rooms = np.append(rooms, room_params["room"])
            count_of_enemies += room_params["count_of_enemies"]
            boss_room = 1
        else:
            room_params = _gen_room(enemy_miltiplier)
            rooms = np.append(rooms, room_params["room"])
            count_of_enemies += room_params["count_of_enemies"]

    return {"rooms_array": rooms, "count_of_enemies": count_of_enemies}
