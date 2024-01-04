import random
import string
from typing import Generator


class Cracker:
    """
    Include any of the options shown below.  Number of tries is required.  Also, must include max_len or known_len.
    Tries will be the number of string generations.
    When including max_len it's recommended to include min_len as well.
    Including known_len will make the set of guesses a fixed length and ignore the other len parameters.
    Using no options produces only lowercase letters.  While other options include lowercase by default,
    Using the "digitsonly" option will only have digits, useful for numeric pins.

    Cracker(options=["uppercase", "digits", "symbols", "digitsonly"], params={tries: int, [prefix: str, max_len: num, min_len: num, known_len: num]})
    """

    charset: str
    max_len: int
    min_len: int
    tries: int
    fixed: bool = False
    prefix: str = ""

    def __init__(self, *options, **params) -> None:
        self.tries = 0 if "tries" not in params else params["tries"]
        self.prefix = "" if "prefix" not in params else params["prefix"]

        if self.tries == 0:
            raise "Please include tries=number_of_tries"

        # Initialize the parameters
        if "known_len" in params:
            self.fixed = True
            self.max_len = params["known_len"]
        elif "max_len" in params:
            self.max_len = params["max_len"]
            if "min_len" in params:
                self.min_len = params["min_len"]
        else:
            raise "Please include a known_len or a max_len!"

        # Build the charset
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
        num_chars = (
            self.max_len - len(self.prefix)
            if self.fixed
            else random.randrange(self.min_len, self.max_len + 1) - len(self.prefix)
        )
        return self.prefix + ("".join(random.choices(self.charset, k=num_chars)))

    def generate_guesses(self) -> Generator[str, str, str]:
        return (self.generate_string() for _ in range(self.tries))
