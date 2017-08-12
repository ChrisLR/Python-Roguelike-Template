"""
This is the scene module. 
"""
import abc
from clubsandwich.director import Scene


class BaseScene(Scene):
    """Abstract class for all scenes"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, game_context):
        super().__init__()
        self.game_context = game_context
        self.active_windows = []

    def render(self, active):
        if self.active_windows:
            self.active_windows[0].render(True)

    def handle_input(self, key_events, mouse_events):
        for key_event in key_events:
            if key_event.keychar == "ESCAPE":
                self.close_window()

        if self.active_windows:
            self.active_windows[0].handle_input(key_events, mouse_events)

    def invoke_window(self, window):
        self.active_windows.insert(0, window)

    def close_window(self):
        if len(self.active_windows) > 1:
            self.active_windows.pop(0)
            return

    def transition_to(self, scene):
        self.director.replace_scene(scene)

    def terminal_read(self, char):
        self.handle_input((char,), (None,))
        super().terminal_read(char)

    def terminal_update(self, is_active=False):
        self.render(is_active)
        super().terminal_update(is_active)
