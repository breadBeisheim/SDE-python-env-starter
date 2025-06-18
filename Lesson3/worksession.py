# Instruction is to, "In sticking with the food theme, 
# create all the variables you would need to make your 
# favorite breakfast, lunch, or dinner. Practice using 
# different types of variables (strings, integers, 
# floats, and booleans). You can also include comments
#  to leave notes to yourself about what you are 
# creating and if you struggled with anything.
#  You can print all the ingredients by using
#  print(put ingredient name here). Be as creative as 
# you would like!"

# First I create a recipe:

recipeList = ["Cheese", "Pastry sheets", "Egg", "Feta Cheese"]

# Then I make a list of imaginary times for printing 
# later to demonstrate booleans, integers and flows.

recipeTime = ["2", "450"]
waitTime = [2.5]
isItGood = True

# I make a function to print recipies next.

def banitzaRecipe():
    for item in recipeList:
        print(f"You will need {item}")

def banitzaInstructions(time, temp):
    print(f"To make it you need to put it in the oven for {time} hours at {temp} degrees farienheit.")

# Then I print everything.

banitzaInstructions(recipeTime)
banitzaRecipe()
