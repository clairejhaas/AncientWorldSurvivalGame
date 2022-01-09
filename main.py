import time
print("")
print("------------------------------------------------------ ")
print("Welcome to the Humanities of the Early World text game! ") 
time.sleep(1)
print("Note: game works best on a full screen. ") 
time.sleep(1)
print("You will read a variety of prompts which replicate the Ancient World. ")
time.sleep(1)
print("You will have to make a series of decisions based on these prompts. ")
time.sleep(1)
print("Based on historical research (sources provided), you will receive a factual outcome of your decision. ")
time.sleep(1)
print("View sources on github at 'https://github.com/clairehaaas/AncientWorldSurvivalGame'. Designed by @clairehaaas. ") 
time.sleep(1)
print("You will start with 40 health points (points are awarded for correct responses). ")
time.sleep(1)
print("The game will continue the game until you lose all your points. ")
time.sleep(1)
print("You can win by getting 150 health points. Good luck. ")
print("")
time.sleep(3)

hp = 40

def get_input(prompt, accepted):
  while True:
      value = input(prompt).lower()

      if value in accepted:
        return value
      else:
        print("Sorry, but your answer is not a recognized answer. Please type one of ", accepted)
print("Would you like to hear modern day connections about the Ancient World? ")
commentary = get_input("Yes or no? ",["yes","no"])
print("")

def commentaryModeOn():
    print ("Commentary mode: on.")

def commentaryModeOff():
    print ("Commentary mode: off.")

if commentary == "yes":
  commentaryModeOn()
  exec(open("commentary.py").read())
elif commentary == "no":
  commentaryModeOff()
  exec(open("nocommentary.py").read())