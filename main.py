import glob
import os
import os.path

import arcade

import header as h
import inside

maps = glob.glob(h.MAPS_PATH % "*")
for map in maps:
    os.remove(map)


if os.path.isfile("game.json"):
    os.remove("game.json")


class Dante(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, window_name):
        """
        Initializer
        """
        super().__init__(width, height, window_name)
        # Sprite lists
        self.all_sprites_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None
        self.floor_list = None
        self.physics_engine = None

        self.act_name = h.ACT_CHRONO[0]
        self.dangeon_map = inside.map.Map(self.act_name)

        self.curent_map = ""

    def draw_room(self):

        self.all_sprites_list = arcade.SpriteList()
        self.floor_list = arcade.SpriteList()

        for x in range(173, 650, 64):
            floor = arcade.Sprite(h.RES % ("texture", h.TEXTURE_FILE_NAME %
                                           ("floor", self.act_name, 1)), h.SPRITE_SCALING)
            floor.center_x = x
            floor.center_y = 200
            self.all_sprites_list.append(floor)
            self.floor_list.append(floor)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.floor_list.draw()


def main():
    """ Main method """
    window = Dante(h.WIN_WIDTH, h.WIN_HEIGHT, "DANTE")
    window.draw_room()
    arcade.run()


if __name__ == "__main__":
    main()
