from anyapp import AppUser, UserSystem
from cracker import Cracker


my_cracker = Cracker("uppercase", max_len=4, tries=10000000)
my_cracker.set_guess_generator()

my_system = UserSystem()
test_pw = "teST"
user = AppUser(id=1, name="makool", password=test_pw)
my_system.add_user(user)
user = my_system.get_user("makool")
print(user.check_password(test_pw))

print(f"Password is: {my_cracker.guess(user.check_password)}")