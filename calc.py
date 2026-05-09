import tkinter as ttk
from enum import Enum
import random
import time


class ValueType(Enum):
    NUMBER = 1
    OPPERATOR = 2
    SPECIAL = 3
    EQUALS = 4


class State(Enum):
    MATHING = "Mathing"
    ERROR = "Error"
    SOLVED = "Solved"


class Calc:

    BUTTONS: dict[str, None | ttk.Button] = {
        "zero": None,
        "one": None,
        "two": None,
        "three": None,
        "four": None,
        "five": None,
        "six": None,
        "seven": None,
        "eight": None,
        "nine": None,
        "decimal": None,
        "add": None,
        "subtract": None,
        "multiply": None,
        "divide": None,
        "left parentheses": None,
        "right parentheses": None,
        "percent": None,
        "delete": None,
        "equals": None,
    }

    BASE_HEIGHT = 3
    BASE_WIDTH = 6
    BUTTON_FONT = ("arial", 16)
    LABEL_FONT = ("arial", 10, "bold")

    NUMBER_BUTTON_COLOR = "#cd6889"
    OPERATOR_BUTTON_COLOR = "#6959cd"
    SPECIAL_BUTTON_COLOR = "#20b2aa"

    TEXT_COLOR = "#000000"
    BACKROUND_COLOR = "#ffffff"

    def __init__(
        self,
        makes_guesses: bool = False,
        scrambles_buttons: bool = False,
    ) -> None:
        self._root = ttk.Tk()

        self._makes_guesses: bool = makes_guesses
        self._scrambles_buttons: bool = scrambles_buttons

        self._equation = ""
        self._solved = False
        self._last_interaction = None

        self._setup_window()
        self._initialize_frame()

        self._initialize_number_buttons()
        self._initialize_operator_buttons()
        self._initialzie_special_buttons()
        self._initialize_equal_button()
        self._initialize_display()

    def _setup_window(self):
        root = self._root

        root.title("Calc (slang for calculator)")
        # root.iconbitmap(r"icon.ico")
        root.resizable(False, False)
        root.config(bg=self.BACKROUND_COLOR)

    def _initialize_frame(self):
        root = self._root

        button_box = ttk.Frame(root, name="button frame")
        button_box.grid(column=0, row=1, columnspan=4, rowspan=5)

        self._button_frame = button_box

    def _initialize_number_buttons(self):
        button_frame = self._button_frame

        BUTTON_NAMES = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "decimal",
        ]

        # creates button for 0
        current_button_index = 0
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text="0",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.NUMBER_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(row=4, column=1)
        button.config(command=lambda: self._extend_equation("0", ValueType.NUMBER))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

        # creates buttons for 1-9
        number = 0
        for row in range(1, 4):
            for column in range(3):

                current_button_index += 1
                number += 1

                button = ttk.Button(
                    button_frame,
                    name=BUTTON_NAMES[current_button_index],
                    text=str(number),
                    height=self.BASE_HEIGHT,
                    width=self.BASE_WIDTH,
                    fg=self.TEXT_COLOR,
                    bg=self.NUMBER_BUTTON_COLOR,
                    font=self.BUTTON_FONT,
                )
                button.grid(row=row, column=column)
                button.config(
                    command=lambda number=number: self._extend_equation(
                        str(number), ValueType.NUMBER
                    )
                )
                self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

        # create button decimal
        current_button_index += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text=".",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.NUMBER_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(row=4, column=0)
        button.config(command=lambda: self._extend_equation(".", ValueType.NUMBER))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

    def _initialize_operator_buttons(self):
        button_frame = self._button_frame

        BUTTON_NAMES = ["add", "subtract", "multiply", "divide"]

        # create button add
        current_button_index = 0
        current_column = 3
        current_row = 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text="+",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.OPERATOR_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("+", ValueType.OPPERATOR))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

        # create button subtract
        current_button_index += 1
        current_row += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text="-",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.OPERATOR_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("-", ValueType.OPPERATOR))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

        # create button multiply
        current_button_index += 1
        current_row += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text="*",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.OPERATOR_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("*", ValueType.OPPERATOR))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

        # create button divide
        current_button_index += 1
        current_row += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text="/",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.OPERATOR_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("/", ValueType.OPPERATOR))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

    def _initialize_equal_button(self):
        button_frame = self._button_frame

        BUTTON_NAMES = ["equals"]

        # create button equals
        current_button_index = 0
        current_column = 2
        current_row = 4
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_button_index],
            text="=",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.SPECIAL_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("=", ValueType.EQUALS))
        self.BUTTONS[BUTTON_NAMES[current_button_index]] = button

    def _initialzie_special_buttons(self):
        button_frame = self._button_frame

        BUTTON_NAMES = ["left parentheses", "right parentheses", "percent", "delete"]

        # create button left parentheses
        current_name_index = 0
        current_column = 0
        current_row = 0
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_name_index],
            text="(",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.SPECIAL_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("(", ValueType.SPECIAL))
        self.BUTTONS[BUTTON_NAMES[current_name_index]] = button

        # create button right parentheses
        current_name_index += 1
        current_column += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_name_index],
            text=")",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.SPECIAL_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation(")", ValueType.SPECIAL))
        self.BUTTONS[BUTTON_NAMES[current_name_index]] = button

        # create button left percent
        current_name_index += 1
        current_column += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_name_index],
            text="%",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.SPECIAL_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=lambda: self._extend_equation("%", ValueType.SPECIAL))
        self.BUTTONS[BUTTON_NAMES[current_name_index]] = button

        # create button backspace
        current_name_index += 1
        current_column += 1
        button = ttk.Button(
            button_frame,
            name=BUTTON_NAMES[current_name_index],
            text="<-",
            height=self.BASE_HEIGHT,
            width=self.BASE_WIDTH,
            fg=self.TEXT_COLOR,
            bg=self.SPECIAL_BUTTON_COLOR,
            font=self.BUTTON_FONT,
        )
        button.grid(column=current_column, row=current_row)
        button.config(command=self._backspace)
        self.BUTTONS[BUTTON_NAMES[current_name_index]] = button

    def _initialize_display(self):

        root = self._root

        # create label for equation
        display = ttk.Label(
            root,
            name="display",
            text="",
            wraplength=240,
            justify="left",
            height=self.BASE_HEIGHT,
            fg=self.TEXT_COLOR,
            bg=self.BACKROUND_COLOR,
            font=self.LABEL_FONT,
        )
        display.grid(row=0, column=1, columnspan=3, sticky="E")

        # create label for mode
        state_display = ttk.Label(
            root,
            name="state_display",
            text=State.MATHING.value,
            fg=self.TEXT_COLOR,
            bg=self.BACKROUND_COLOR,
            font=self.LABEL_FONT,
        )
        state_display.grid(row=0, column=0, columnspan=2, sticky="W")

        self._display = display
        self._state_display = state_display

    def _backspace(self):

        self._equation = self._equation[:-1]

        self._display.config(text=self._equation)
        print(f"DEBUG: {self._equation}")

    def _update_display(self, val: str | None = None):
        if val is None:
            self._display.config(text=self._equation)

        else:
            self._display.config(text=val)

    def _update_state_display(self, state: State):
        self._state_display.config(text=state.value)

    def _extend_equation(self, val, action: ValueType):

        if self._scrambles_buttons == True:
            self._scramble_buttons()

        if self._solved == True:
            self._update_display()
            self._update_state_display(State.MATHING)
            self._solved = False

        if action == ValueType.NUMBER:
            self._last_interaction = ValueType.NUMBER

            self._equation += val
            self._update_display()

        elif action == ValueType.OPPERATOR:
            # stops user form having 2 opperators in a row
            if self._last_interaction == ValueType.OPPERATOR:
                return
            self._last_interaction = ValueType.OPPERATOR

            self._equation += val
            self._update_display()

        elif action == ValueType.SPECIAL:
            self._equation += val
            self._update_display()

        elif action == ValueType.EQUALS:

            math_sum = self._solve()

            self._equation = ""
            self._last_interaction = None
            self._solved = True

            # check when divided by zero
            if math_sum == None:
                self._update_state_display(State.ERROR)
                self._update_display("=NaN")
                return

            if self._makes_guesses == True:
                self._make_guesses(math_sum)

            if math_sum == int(math_sum):
                self._update_display(f"={int(math_sum)}")

            else:
                self._update_display(f"={math_sum}")

            self._update_state_display(State.SOLVED)

        print(f"DEBUG: {self._equation}")

    def _solve(self):

        return eval(self._equation)

    def run(self):

        self._root.mainloop()

    # information functions
    def print_buttons(self):
        """Prints a list of buttons"""

        for key, button in zip(self.BUTTONS.keys(), self.BUTTONS.values()):
            if button is not None:
                print(f"{key}: {button.cget("text")}")

    def print_button_positions(self):
        """Prints the position of each button
        example output:
        >>> button: column-0 row-0"""

        for button in self.BUTTONS.values():
            if button is not None:
                button_info = button.grid_info()
                print(
                    f"{button}: column-{button_info['column']} row-{button_info['row']}"
                )

    # bad features
    def _make_guesses(self, math_sum):

        def generate_numbers(x, y):
            numbers = []
            for _ in range(x):
                num = random.randint(1, 10**y - 1)
                numbers.append(num)
            return numbers

        display = self._display

        length = len(str(abs(math_sum)))

        guess_list = generate_numbers(250, length)
        guess_list.append(math_sum)

        random.shuffle(guess_list)

        self._state_display.config(text="Guessing")

        guess = guess_list.pop()
        while guess != math_sum:

            display.config(text=guess)
            self._root.update()
            guess = guess_list.pop()
            time.sleep(0.1)

    def _scramble_buttons(self):

        button_positions: list[tuple[int, int]] = []

        for button in self.BUTTONS.values():
            if button is None:
                return

            button_info = button.grid_info()
            button_positions.append((button_info["column"], button_info["row"]))

        random.shuffle(button_positions)

        current_index = 0
        for button in self.BUTTONS.values():
            if button is None:
                return

            button.grid(
                column=button_positions[current_index][0],
                row=button_positions[current_index][1],
            )

            current_index += 1


def main():

    app = Calc(True, True)
    app.run()


if __name__ == "__main__":
    main()
