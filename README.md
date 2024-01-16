# Cracker!
A fun Python project to show off advanced features of the language for brute-force password attacks and web app simulation.  
### Background
With a brute-force password attack, you have to make a bunch of guesses.  This type of attack is usually not possible today on the webs with so many features in place to prevent this.  But it's still a neat concept to play with to understand some of things you would need to make it work, as well as optimizing Python to go fast!  

## Cracker
With the Cracker class, we're showing off how you can unpack `*options` and `**params` in the initializer.  
You can create an instance with your options first and then add some named parameters, which will raise an exception if you don't include the required ones.  
So, you could have: `my_cracker = Cracker("digits", prefix="test", max_len=8, min_len=5, tries=10000000)`  
or at the least: `my_cracker = Cracker(known_len=6, tries=10)`  
This style keeps the class signature simple and allows some logic in the initialization.  
The idea being, I can start with a few simple features like random generation and including a prefix.  While it could be extended to add more features later, like dictionary attack.  
### Generator
In the first iteration of this, I used the lovely `generate_string()` function to fill up a giant list the size of the number of tries.  
As soon as you get to 10M, it becomes a problem for your memory.  
So, that became the `generate_passwords()` function, which returns a list of passwords using the settings you initialized.  
On the other hand, the `set_guess_generator()` function uses a _generator expression_ which informs Python _how_ to create a list, and thus your memory is preserved.  
The `guess(check_password_function)` function accepts a function as an argument.  Iterating with the generator, the elements are borne on the fly, which kinda seems like magic... now you just have to check all your 10M guesses against a user system!  Hence, I allow the check_password_function, which accepts one argument as the check and returns a bool.  So, you could wrap any external system in your check function and pass it through.  

## AnyApp
Of course, the bottleneck for any brute-force attack is: checking the password against the guesses.  So I also created a dummy app called: AnyApp.  
For now, it's just a UserSystem which showcases Pydantic nested classes as well as password hashing and checking.  

> Formatted with Black because I like that...

# What to do next?
The only way this would be potentially useful is, say you happened to get a database dump of usernames and hashed passwords.  If you also knew a few parameters of what's expected to make up passwords... (see how that could actually be a security flaw rather than a feature?)  If you also knew the hashing algorithm used, and had enough time on your hands, you might be able to crack a few passwords.  
- Threading: Iterating over 10M guesses is taking me at most 30 seconds.  You could chunk up the guesses somehow and run multiple threads at the same time.  
- Passing in the available charset 
- Main is the just the test file for now, but it could be made to orchestrate more.
- Actual tests: pytest or unittest