from anyapp import AppUser, UserSystem
from cracker import Cracker

# Initilize the Cracker
my_cracker = Cracker("uppercase", "symbols", "digits", max_len=13, tries=12)
my_cracker.init_guess_generator()

# Initialize the User System
my_system = UserSystem()
test_pw = "teST"
user = AppUser(id=1, name="makool", password=test_pw)
my_system.add_user(user)

print(f"Password check works: {user.check_password(test_pw)}")
print(f"Password is: {my_cracker.guess(user.check_password)}")