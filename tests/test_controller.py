import copy
import random

from game.controller import Controller


def test_controller():
    from kivy.logger import LOG_LEVELS, Logger

    Logger.setLevel(LOG_LEVELS["debug"])

    c = Controller()
    c.setup()
    # advance 3 rounds
    for _ in range(3):
        for i in copy.deepcopy(c.sequence):
            c.play(i)

    # press wrong button
    all_buttons = set(range(c.button_count))
    Logger.debug(f"App: {all_buttons=}")
    wrong_buttons = list(all_buttons - {c.sequence[0]})
    Logger.debug(f"App: {wrong_buttons=}")
    assert not c.game_is_over
    c.play(random.choice(wrong_buttons))
    assert c.game_is_over

    # press wrong button at the end of round 2
    c.setup()
    for k in range(2):
        for j, i in enumerate(copy.deepcopy(c.sequence)):
            if k == 1 and j == 1:
                continue
            c.play(i)
    wrong_buttons = list(all_buttons - {c.sequence[0]})
    c.play(random.choice(wrong_buttons))
