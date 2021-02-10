from typing import Callable, Tuple


class Logic():
    def __init__(cords=(37.620070, 55.753630), zoom_level=10, map_type='map', render_callback: Callable):
        self.cords = cords
        self.zoom_level = zoom_level
        self.map_type = map_type
        self.render_map = render_callback
        self.step = 0.15

    @render_callback
    def move(self, dirc: Tuple[int, int]):
        x = cords[0] += dirc[0] * (self.zoom_level // 100) * self.step
        y = cords[1] += dirc[1] * (self.zoom_level // 100) * self.step

    @render_callback
    def change_zoom(self, change: int):
        if 0 <= self.zoom_level + change <= 17:
            self.zoom_level += change

    @render_callback
    def change_map(self, map_t: str):
        if map_t not in ['map', 'sat', 'sat, skl']:
            raise NameError("""Only 'map', 'sat', 'sat, skl' """)
        self.map_type = map_t
