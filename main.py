from anyapp import AppUser, UserSystem
from cracker import Cracker


my_cracker = Cracker("digits", prefix="test", max_len=8, min_len=6, tries=10000000)
guesses = my_cracker.generate_guesses()

my_system = UserSystem()
test_pw = "test2434"
user = AppUser(id=1, name="makool", password=test_pw)
my_system.add_user(user)
user = my_system.get_user("makool")
print(user.check_password(test_pw))

def guess() -> str:
    for g in guesses:
        if user.check_password(g):
            print("Cracked!")
            return g
    return "not cracked :("

print(f"Password is: {guess()}")