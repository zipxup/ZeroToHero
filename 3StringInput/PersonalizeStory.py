#initialize variables;
girlDescription = " "
boyDescription = " "
walkDescription = " "
girlName = " "
boyName = " "
animal = " "
gift = " "
answer = " "

#users to specify values for the variables
girlName = input("Enter a girl's name: ")
boyName = input("Enter a boy's name: ")
animal = input("Name a type of animal: ")
gift = input("Name something you find in your room: ")
girlDescription = input("Enter a description of a girl: ")
boyDescription = input("Enter a description of a boy: ")
walkDescription = input("Enter a description of how you might dance: ")
answer = input("What would you say to someone who gave you a flower: ")

#Display the story
print ("Once upon a time,")
print("there was a girl named " + girlName.capitalize() + ".")
print("One day, " + girlName.capitalize() + " was walking " + walkDescription.lower() + " down the street.")
print("Then she met a " + boyDescription.lower() + " boy named " + boyName.capitalize() + ".")
print("He said, 'You are really " + girlDescription.lower() + "!'")
print("She said '" + answer.capitalize() + ", " + boyName.capitalize() + ".'")
print("Then they both rode away on a " + animal.lower() + " and lived happily ever after.")