import random
from typing import List

from kivy.logger import Logger


class Controller:
    def __init__(self, button_count: int = 4):
        self.button_count = button_count
        self.sequence: List[int] = []
        self.game_is_over = False

    def setup(self):
        self.sequence = []
        self.player_sequence = []
        self.game_is_over = False
        self.append_to_sequence()

    def append_to_sequence(self):
        self.sequence.append(random.randint(0, self.button_count - 1))
        Logger.debug(f"App: Current sequence: {self.sequence}")

    def play(self, move: int):
        self.player_sequence.append(move)
        Logger.debug(f"App: Player moves: {self.player_sequence}")
        if len(self.player_sequence) == len(self.sequence):
            if self.player_sequence == self.sequence:
                self.advance_to_next_round()
            else:
                self.game_over()
        else:
            if self.player_sequence != self.sequence[: len(self.player_sequence)]:
                self.game_over()

    def advance_to_next_round(self):
        Logger.debug("App: advancing to next round")
        self.player_sequence = []
        self.append_to_sequence()

    def game_over(self):
        Logger.debug("App: game over")
        self.game_is_over = True
