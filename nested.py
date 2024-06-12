#Lesson 2: Assignments: Nested If

# 1. Nested Decisions: The Adventure Game 🏰

#place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
if place == "cave":
    print("You find a hidden treasure!")
elif action == "cross a river":
     print("You found a boat!")

#Task 2: Setting the Scene

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")

if place == "cave":
   scene = (input('Do you want to "light a torch" or "proceed in the dark"?'))
if scene == ("light a torch"):
    print("Great Job lighting your torch")
if scene == ("proceed in the dark"):
    print ('Dark here I come !')

#Task 3: Default Path

if place == "forest":
     if (place  != ('forest' or 'cave')):
         pass
     action = input("climb a tree or cross a river?")
     if (action != ('climb a tree' or 'cross a river')):
         pass
     if action == "climb a tree":
         print("You found a bird's nest!")
     elif action == "cross a river":
         print("You found a boat!")

if place == "cave":
     scene = (input('Do you want to "light a torch" or "proceed in the dark"?'))
     if scene != ('light a torch' or 'proceed in the dark'):
       pass
     if scene == ("light a torch"):
        print("Great Job lighting your torch")
     if scene == ("proceed in the dark"):
         print ('Dark here I come !')


#Task 1: Code Correction

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)


attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2: Catering Choices

food = input ('Do you want vegetarian food ?')
food_choice = 'Veggie Delight Caterers' if food == 'yes' else 'Gourmet Meals Caterers' 
print(food_choice)