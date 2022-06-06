import functools

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.uix.button import Button

from .controller import Controller

FLASH_TIME = 2


class Game(App):
    def build(self):
        self.load_kv()
        self.controller = Controller()
        self.controller.setup()

        colors = ("yellow", "blue", "red", "green")
        buttons = []
        for i, color in enumerate(colors):
            button = Button(
                background_color=color,
                background_normal="",
                background_disabled_normal="",
            )
            button.number = i
            self.root.ids.grid.add_widget(button)
            buttons.append(button)

        def set_button(button_id, _):
            Logger.info(f"GUI: flashing {buttons[button_id].number}")
            buttons[button_id].background_color = "white"

        def unset_button(button_id, _):
            Logger.info(f"GUI: flashed {buttons[button_id].number}")
            buttons[button_id].background_color = colors[button_id]

        def flash_buttons():
            Logger.info(f"Controller: sequence is {self.controller.sequence}")

            for button in buttons:
                button.disabled = True

            for i, button_id in enumerate(self.controller.sequence):

                Clock.schedule_once(
                    functools.partial(set_button, button_id), i * FLASH_TIME
                )
                Clock.schedule_once(
                    functools.partial(unset_button, button_id),
                    (i + 0.4) * FLASH_TIME,
                )

            def enable_buttons(_):
                for button in buttons:
                    button.disabled = False

            Clock.schedule_once(
                enable_buttons, FLASH_TIME * len(self.controller.sequence)
            )

        for i, button in enumerate(buttons):

            def move(button):
                Logger.info(f"GUI: making move on {button.number}")
                self.controller.play(button.number)
                if self.controller.game_is_over:
                    self.root.ids.game_over_widget.opacity = 1
                elif len(self.controller.player_sequence) == 0:
                    flash_buttons()

            button.bind(on_press=move)
        flash_buttons()


def main():
    Game().run()


if __name__ == "__main__":
    main()
