import time

print("Welcome to the Humanities of the Early World text game. You will read a variety of prompts which replicate the Ancient World. You will have to make a series of decisions based on these prompts. Using historical research, you will receive the real outcome of your decision. You will start with 40 health points and will continue the game until you lose or find the time portal at the end of your journey. Good luck. ")


hp = 40

def get_input(prompt, accepted):
  while True:
      value = input(prompt).lower()

      if value in accepted:
        return value
      else:
        print("This is not a recognized answer, must be of ", accepted)

def handle_room(location):
  global hp
  if location == "start":
    print("You are standing in front of three time portals. You have three options. The left portal will take you to Ancient Egypt (around 2900 BCE). The straight portal will take you to Athens, Greece (around 350 BCE). The right portal will take you to the Han Dynasty in China (around 200 BCE).")
    direction = get_input("What portal will you select? Left, straight, or right? ",["left","right", "straight"])

    if direction == "left":
      return "egypt"
    elif direction == "straight":
      return "greece"
    elif direction == "right":
      return "china"
    

  elif location == "egypt":
      print("You arrive in Ancient Egypt. ")
      print("A small snake bites you, and you lose 20 health points. ")
      hp = hp - 20

      answer = get_input("Do you want to go to the pyramid scheme? ", ["yes", "no"])
      if answer == "yes":
        return "deep_cave"
      else:
        return "start"

    elif location

  elif location == "beach":
    print("You walk to the beach but remember you do not have any swimwear. ")
    print("The cool water revitalizes you. You have never felt more alive, you 
    gain 70 health points. ")
    hp += 70

    return "end"
  else:
    print("Programmer error, room", location, " is unkown")
    return "end"

location = "start"
while location != "end":
  location = handle_room(location)

  print("You have", hp, "health points.")
  if hp <= 0:
    print("You did not survive the ancient world.  ")
    print("Your adventure has ended, goodbye.")
    break

