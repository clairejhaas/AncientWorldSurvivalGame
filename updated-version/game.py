import time


def get_input(prompt, accepted):
    while True:
        value = input(prompt).lower()

        if value in accepted:
            return value
        else:
            print("Sorry, but your answer is not a recognized answer. Please type one of ", accepted)


def handle_room(location):
    global hp
    if location == "start":

        if not with_commentary:
            time.sleep(2)

        print("You are standing in front of three time portals. You have three options. ")
        time.sleep(1)
        print("The left portal will take you to Ancient Egypt (around 2900 BCE). ")
        time.sleep(1)
        print("The straight portal will take you to Athens, Greece (around 350 BCE). ")
        time.sleep(1)
        print("The right portal will take you to the Han Dynasty in China (around 200 BCE). ")
        time.sleep(1)
        direction = get_input("What portal will you select? Left, straight, or right? ", ["left", "right", "straight"])

        if direction == "left":
            return "egypt"
        elif direction == "straight":
            return "greece"
        elif direction == "right":
            return "china"

    elif location == "egypt":
        print("")
        print("You arrive in Ancient Egypt. ")
        print("As you walk around, you see two groups of people. Some are doctors (option 1), others are farmers (option 2). ")
        time.sleep(1)
        option = get_input("Which option do you choose? 1 or 2? ", ["1", "2"])

        if option == "1":
            return "doctor_egyptian"
        else:
            return "farmer_egyptian"

    elif location == "doctor_egyptian":
        print("As you talk with the local doctors, they explain that people are getting sick for some reason. ")
        time.sleep(1)
        print("You decide to go to the Egyptian court to present your case. How does the government react? ")
        doctor_egyptian_react = get_input("Good or bad? ", ["good", "bad"])

        if doctor_egyptian_react == "good":
            print("This is the correct choice. Gain 20 pts. The Egyptian government trusted scientists and listened to the people. ")
            hp += 20
            print(f"You have {hp} health points")
            time.sleep(1)
            print("The court tells you to list off the symptoms that many Ancient Egyptians are facing. ")
            time.sleep(1)
            print("The Egyptians are facing pain when going to the bathroom, when drinking, and itchy skin (Abdel-Ghaffar). ")
            doctor_egyptian_disease_answer = get_input("What is the source of the disease? Water or climate? ", ["water", "climate"])

            if doctor_egyptian_disease_answer == "water":
                print("This is the correct choice. Gain 20 points. ")
                hp += 20
                print("You have", hp, "health points.")
                time.sleep(1)
                print("Water pollution was a problem for Egyptians. Luckily, the Egyptians learned how to prevent polution (Butrous). ")
                time.sleep(1)
                print("Due to the positive relationship between the Egyptian government and the Egyptian doctors, many of the Egyptian population was able to be cured. ")

                if with_commentary:
                    time.sleep(2)
                    print("This is an effective lesson for the modern day government to listen to experts and try to keep water sources clean. ")

                print("")
                time.sleep(3)
                cycle = get_input("Go back to Egypt (option 1) or portal (option 2)? 1 or 2? ", ["1", "2"])

                if cycle == "1":
                    return "egypt"
                else:
                    return "start"

            elif doctor_egyptian_disease_answer == "climate":
                print("This is incorrect. Lose 20 points. While climate caused many Egyptians to develop respiratory illnesses, the symptoms were not related to climate (Butrous). ")
                time.sleep(2)

                if with_commentary:
                    print("Listening is important when dealing with the relationship between government and people. Ancient Egypt developed a strong listening relationship which should be considered. ")

                hp -= 20
                print("You have", hp, "health points.")
                print("")
                time.sleep(3)
                print("Returning to the portal... ")
                print("")
                return "start"

        elif doctor_egyptian_react == "bad":
            print("This is incorrect. Egyptians actually respected doctors. Under this era, medicine thrives and there are several medical papyrus records (Butrous). Lose 20 health points. ")
            
            if with_commentary:
                time.sleep(2)
                print("By studying the Ancient World, modern day governments can learn that trusting doctors and scientists makes for a healthier and happier population. ")
            time.sleep(1)

            if with_commentary:
                print("Following the example of the Egyptians and their embrace of science will lead to innovation. ")
                time.sleep(1)

            hp -= 20
            print("You have", hp, "health points.")
            print("")
            time.sleep(3)
            print("Returning to the portal... ")
            print("")
            return "start"

    elif location == "farmer_egyptian":
        print("As you talk with the local farmers, they explain that the crops are dying for some reason. You decide to go to the Egyptian court to present your case. How does the government react? ")
        farmer_egyptian_react = get_input("Good or bad? ", ["good", "bad"])

        if farmer_egyptian_react == "good":
            print("This is incorrect. Lose 20 points. The government severely punished farmers who did not meet the grain quotas which were enforced by the pharaoh. ")
            time.sleep(2)

            if with_commentary:
                print("The inequality between the rich and poor is something that the United States should fear today. ")
                time.sleep(1)
                print("Since Egypt was heavily dependent on agriculture, the modern day can learn how important it is to protect the farmers and working class. ")

            hp -= 20
            print("You have", hp, "health points.")
            print("")
            time.sleep(3)
            print("Returning to the portal... ")
            print("")
            return "start"

        elif farmer_egyptian_react == "bad":
            print("This is correct. Since the pharaoh owned the land, the farmers only got to keep a portion of the grain that they farmed (Ruddell). ")
            time.sleep(1)
            print("This resulted in tension between the working class and the poor. Gain 20 health points. ")
            hp += 20
            print("You have", hp, "health points.")
            time.sleep(1)
            print("As the farmers go back to their land, they realize that they need to irrigate the land. ")
            print("They must decide where to place the irrigation systems. ")
            time.sleep(1)
            print("The crops that they are growing are barley, wheat, and rye. Which irrigation system should they build? ")
            farmer_egyptian_irrigation_answer = get_input("Hydraulics or ponds? ", ["hydraulics", "ponds"])

            if farmer_egyptian_irrigation_answer == "hydraulics":
                print("This is the correct choice. Gain 20 points. ")
                hp += 20
                print("You have", hp, "health points.")
                print("Building hyraulics which could move large amounts of water for long periods of time. ")
                time.sleep(1)
                print("The development of dykes and hydraulics increased Egyptian productivity (Janick). ")
                time.sleep(2)

                if with_commentary:
                    print("Since the Egyptians invested in infrastructure, modern day states should do the same. ")
                    time.sleep(1)
                    print("Investing in infrastructure may be a steep climb at first; however, the payment will be worth it in the long term. ")
                    time.sleep(1)
                    print("This relates to the United States infrastructure bill because the US is starting to value infrastructure. ")

                print("")
                time.sleep(3)
                cycle = get_input("Go back to Egypt (option 1) or portal (option 2)? 1 or 2? ", ["1", "2"])

                if cycle == "1":
                    return "egypt"
                else:
                    return "start"

            elif farmer_egyptian_irrigation_answer == "ponds":
                print("This is incorrect. Lose 10 points. While irrigation ponds were used, the ponds required manual labor and were typically only used for fruit trees (Janick). ")
                time.sleep(2)
                print("In Ancient Egypt, the poor would often be the ones to complete the intensive manual labor, while the rich would enjoy the fruits of the labor. ")
                hp -= 10
                print("You have", hp, "health points.")
                print("")
                time.sleep(3)
                print("Returning to the portal... ")
                return "start"
            else:
                return "farmer_egyptian"

    elif location == "greece":
        print("Ancient Athens, Greece is currently not safe to travel to. ")
        print("Please check in again soon. ")
        print("Returning to the portal... ")
        print("")
        return "start"
        
    elif location == "china":
        print("Han China is currently not safe to travel to. ")
        print("Please check in again soon. ")
        print("Returning to the portal... ")
        print("")
        return "start"

    else:
        print("Programmer error, room", location, " does not exist. ")
        return "end"


location = "start"
while location != "end":
    location = handle_room(location)
    
    if hp <= 0:
        print("You did not survive the ancient world.  ")
        print("Your adventure has ended, goodbye. ")
        print("Please play again soon by pressing the run button! ")
        location = "end"
    elif hp >= 150:
        print("You survived the ancient world.  ")
        print("Congratulations! ")
        print("Please play again soon by pressing the run button! ")
        location = "end"
