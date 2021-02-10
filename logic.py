from typing import Callable, Tuple


class Logic():
    def __init__(self, render_callback: Callable, cords=(37.620070, 55.753630), zoom_level=0.01, map_type='map'):
        self.cords = cords
        self.zoom_level = zoom_level
        self.map_type = map_type
        self.render_map = render_callback
        self.step = 0.15

    def move(self, dirc: Tuple[int, int]):
        x = self.cords[0] + dirc[0] * self.step * self.zoom_level
        y = self.cords[1] + dirc[1] * self.step * self.zoom_level
        self.cords = (x, y)
        self.render_map()

    def change_zoom(self, change: float):
        if 0 > self.zoom_level + change:
            return
        self.zoom_level += change
        self.render_map()

    def change_map(self, map_t: str):
        if map_t not in ['map', 'sat', 'sat,skl']:
            raise NameError("""Only 'map', 'sat', 'sat, skl' """)
        self.map_type = map_t
        self.render_map()

    def change_cords(self, cords):
        self.cords = cords
        self.render_map()