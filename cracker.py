import random
import string
from typing import Generator


class Cracker:
    """
    Include any of the options shown below.  Number of tries is required.  Also, must include max_len or fixed_len.
    Tries will be the number of string generations.
    When including max_len it's recommended to include min_len as well.
    Including fixed_len will make the set of guesses a fixed length and ignore the other len parameters.
    Using no options produces only lowercase letters.  While other options include lowercase by default,
    Using the "digitsonly" option will only have digits, useful for numeric pins.

    Cracker(options=["uppercase", "digits", "symbols", "digitsonly"], params={tries: int, [prefix: str, max_len: num, min_len: num, known_len: num]})
    """

    charset: str
    max_len: int
    fixed_len: int = 0
    min_len: int = 1
    tries: int = 0
    prefix: str = ""
    guess_generator: Generator

    def __init__(self, *options, **params) -> None:
        if "tries" in params:
            self.tries = params["tries"]
        if "prefix" in params:
            self.prefix = params["prefix"]

        if self.tries == 0:
            raise BaseException("Please include a number of tries=more_than_zero")

        if "fixed_len" in params:
            self.fixed_len = params["fixed_len"]
        elif "max_len" in params:
            self.max_len = params["max_len"]
            if "min_len" in params:
                self.min_len = params["min_len"]
        else:
            raise BaseException("Please include a fixed_len or a max_len")

        # Build the charset from the options
        charset = string.ascii_lowercase
        if "uppercase" in options:
            charset += string.ascii_uppercase
        if "digits" in options:
            charset += string.digits
        if "symbols" in options:
            charset += string.punctuation
        if "digitsonly" in options:
            charset = string.digits
        print(f"Available charset: {charset}")
        self.charset = charset

    def generate_string(self) -> str:
        if self.fixed_len:
            num_chars = self.fixed_len - len(self.prefix)
        else:
            num_chars = random.randrange(self.min_len, self.max_len + 1) - len(self.prefix)
        return self.prefix + ("".join(random.choices(self.charset, k=num_chars)))

    def set_guess_generator(self):
        self.guess_generator = (self.generate_string() for _ in range(self.tries))

    def generate_passwords(self) -> list[str]:
        return [self.generate_string() for _ in range(self.tries)]

    def guess(self, check_password_function) -> str:
        for g in self.guess_generator:
            if check_password_function(g):
                print("Cracked!")
                return g
        return "not cracked :("