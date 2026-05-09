import random
import time


class Game:

    def __init__(self) -> None:
        self.first_number: int = self._get_number("first")
        self.second_number: int = self._get_number("second")

        self._sum: int = self._get_sum(self.first_number, self.second_number)

        GUESS_DIFFERENCE = 100
        self._guess_list = guess_list = [
            x for x in range(self._sum - GUESS_DIFFERENCE, self._sum + GUESS_DIFFERENCE)
        ]
        random.shuffle(guess_list)

    def _get_number(self, x) -> int:
        while True:
            try:
                number = int(input(f"Enter {x} number: "))
            except:
                continue

            return number
            # if -101 < number < 101:
            #     return number
            # else:
            #     print("number to hard")

    def _get_sum(self, first, second) -> int:
        while True:

            sign = input("+ or - or x or / or exp: ")

            match sign:
                case "+":
                    return first + second
                case "-":
                    return first - second
                case "x":
                    return first * second
                case "/":
                    if self.second_number == 0:
                        print("cant divide by 0")
                        continue
                    return int(first / second)
                case "exp":
                    return first**second
                case _:
                    print("to hard")

    def run(self) -> None:
        while True:
            guess: int = self._guess_list.pop()
            print(f"guessing: {guess}")
            time.sleep(0.1)

            if guess == self._sum:
                print(f"the answer is: {self._sum}")
                break


def main() -> None:
    x = Game()
    x.run()


if __name__ == "__main__":
    main()
