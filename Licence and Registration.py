import random
i = 0
a = 0
b = 0
m = int(500)
randEvent = ["Hitch-hiker", "Police", "Roadwork", "Traffic", "Nothing"]
print ("you have", m, "money")

while i==0:
    choice_1a = str(input("Do uou want to buy a licencse?"))

    if choice_1a == "yes" and a == 0:
        choice_1b = str(input("600 money"))
        
        if m < 300:
            print ("Not enough money")
        
        if choice_1b == "yes":
            m -= 600
            a += 1
            print ("you have", m, "money remaining")
            print (m , a)

        else:
            print("error")

            
    elif a > 0:
        print ("You already bought this item!")
        
    elif choice_1a == "no":
           print ("you still have", m, "money remaining")

    else:
        print("error")





    choice_2a = str(input("Do you want to buy registaration?")).lower()

    if choice_2a == "yes" and b == 0:
        choice_2b = str(input("600 money")).lower()
        if choice_2b == "yes":
            if m < 600:
                print ("Not enough money")
                
            else:
                m -= 600
                print ("you have", m, "money remaining")
                
        elif b > 0:
            print ("You already bought this item!")

        elif choice_2a == "no":
            print ("you still have", m, "money remaining")

        else:
            print("error")

    
    elif choice_2a == "no":
        print ("you still have", m, "money remaining")

    choice_3 = str(input("Do you want to start your shift?")).lower()

    if choice_3 == "yes":
        print ("starting shift...")
        i += 1

    elif choice_3 == "no":
        i += 0

h = 0
j = 0

while h == 0:
    Event =  random.choice(randEvent)

    print("theres", Event)


    if Event == "Roadworks":
        while j == 0:
            choice_4 = str(input("Would you turn back, or go around?"))
            if choice_4 == "turn back":
                print ("Turning Back")
                j += 1

            if choice_4 == "go around":
                print ("Unable go around, try again")
                j += 0

    if Event == "Police":
        while j == 0:
            choice_4 = str(input("Would you turn back, or go around?"))
            if choice_4 == "turn back":
                print ("Turning Back")
                j += 1

            if choice_4 == "go around":
                print ("Going around")

                choice_4a = str(input("The police officer sees you, and starts chasing you, would you pull over, or run"))

                while j==0:
                    choice_4 = str(input("Would you turn back, or go around?"))
                    if choice_4b == "pull over":
                       print ("The police offiver asks for you Licence and Registration")
                       if a == 1:
                           print("You have a licence")
                           if b == 1:
                                print("You have a registration")
                                print("You are free to go!")
                                j += 1

                           if a != 1 and b != 1:
                            print("game over! Your arrested")
                            j += 1

    if Event == "Hitch-hiker":
        print("This event is coming soon")

    if Event == "Traffic":
        while j == 0:
            choice_4 = str(input("Would you turn back, or go around?"))
            if choice_4 == "turn back":
                print ("Turning Back")
                j += 1

            if choice_4 == "go around":
                print ("Unable go around, try again")
                j += 0

    if Event == "Nothing":
        print ("Nothing there carrying on")
            
                








