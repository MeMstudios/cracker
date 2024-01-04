# Cracker!
A fun Python project to show off advanced features of the language for brute-force password attacks and web app simulation.  
### Background
When you think of a brute-force password attack, you have to make a bunch of guesses.  This type of attack is usually not possible today on the webs with so many features in place to prevent this.  But it's still a neat concept to play with to understand some of things you would need to make it work, as well as optimizing Python to go fast!  
## Cracker
With the Cracker class, we're showing off how you can unpack (`*options` and `**params`) in the initializer.  
You can create an instance with your options first and then add some named parameters, which will raise an exception if you don't include the required ones.  
So, you could have: `my_cracker = Cracker("digits", prefix="test", max_len=8, min_len=5, tries=10000000)`  
or at the least: `my_cracker = Cracker(known_len=6, tries=10)`  
It feels kinda like a CLI.  It keeps the class signature simple and allows some logic in the intialization.  
The idea being, I can start with a few simple features like random generation and including a prefix.  While it could be extended to add more features later, like dictionary attack.  
### Generator
The first iteration of this, I used the lovely `generate_string()` function to fill up a giant list.  
(Whatever the number of `tries` is set to.)  
As soon as you get to 10M, it becomes a problem for your memory.  
Look at the function signature and the return value of `generate_guesses()`.  The code for returning a list is very similar:  
`[self.generate_string() for _ in range(self.tries)]` (list interpretation) would work to create a large list of random strings.  
Instead: `(self.generate_string() for _ in range(self.tries))` (generator expression) informs Python how to _create_ a list.  
