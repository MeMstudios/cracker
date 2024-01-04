# Cracker!
A fun Python project to show off advanced features of the language for brute-force password attacks and web app simulation.  
### Background
When you think of a brute-force password attack, you have to make a bunch of guesses.  This type of attack is usually not possible today on the webs with so many features in place to prevent this.  But it's still a neat concept to play with to understand some of things you would need to make it work, as well as optimizing Python to go fast!  

## Cracker
With the Cracker class, we're showing off how you can unpack (`*options` and `**params`) in the initializer.  
You can create an instance with your options first and then add some named parameters, which will raise an exception if you don't include the required ones.  
So, you could have: `my_cracker = Cracker("digits", prefix="test", max_len=8, min_len=5, tries=10000000)`  
or at the least: `my_cracker = Cracker(known_len=6, tries=10)`  
This style keeps the class signature simple and allows some logic in the intialization.  
The idea being, I can start with a few simple features like random generation and including a prefix.  While it could be extended to add more features later, like dictionary attack.  
### Generator
The first iteration of this, I used the lovely `generate_string()` function to fill up a giant list.  
(Whatever the number of `tries` is set to.)  
As soon as you get to 10M, it becomes a problem for your memory.  
Look at the function signature and the return value of `generate_guesses()`.  The code for returning a list is very similar:  
`[self.generate_string() for _ in range(self.tries)]` (list interpretation) would work to create a large list of random strings.  
Instead: `(self.generate_string() for _ in range(self.tries))` (generator expression) informs Python _how_ to create a list.  
When you iterate of the generator, the elements are generated on the fly, which kinda seems like magic... now you just have to check all your 10M guesses against a user system!  

## AnyApp
Of course, the bottleneck for any brute-force attack is: checking the password against the guesses.  So I've also created a dummy app called, AnyApp.  
For now, it's just a UserSystem which showcases Pydantic nested classes as well as password hashing and checking.  

> Formatted with Black because I like that...