import random
import time

d = 0
m = 500

#fix the time var and classes

timevar = 0

def timevar():
    global t
    t = 0

class AddTime():
    def timeadd(self):
        timevar = timevar + 1

class MaxTime():
    def limit(self):
        if timevar > 60:
            timevar = 60


while True:
    i = 0
    a = 0
    b = 0
    k = 0
    #RandEvent = ["Hitch-hiker", "Police", "Roadwork", "Traffic", "Nothing"]
    RandEvent = ["Traffic"]
    RandEventPolice = ["Caught", "Escaped"] #Wrote the list as ["Cuaght, Escaped"] which messed up my whole code
    print ("you have", m, "money")

    while i==0:
        choice_1a = str(input("Do you want to buy a licencse?")).lower()

        if choice_1a == "yes" and a == 0:
            choice_1b = str(input("600 money")).lower()
            
            if m < 300:
                print ("Not enough money")
            
            if choice_1b == "yes":
                m -= 600
                a += 1
                print ("you have", m, "money remaining")
                print (m , a)


                
        elif a > 0:
            print ("You already bought this item!")
            
        elif choice_1a == "no":
            print ("you still have", m, "money remaining")





        choice_2a = str(input("Do you want to buy registaration?")).lower()

        if choice_2a == "yes" and b == 0:
            choice_2b = str(input("800 money")).lower()
            if choice_2b == "yes":
                if m < 800:
                    print ("Not enough money")
                    
                else:
                    m -= 800
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

    while h == 0:
        j = 0
        s = AddTime.timeadd
        
        foo = MaxTime()
        foo.limit()

        print("Money: ", m)

        Event =  random.choice(RandEvent)

        print("theres", Event)

        if Event == "Roadwork":
            while j == 0:
                choice_4 = str(input("Would you turn back, go through, or go around?")).lower()
                if choice_4 == "turn back":
                    print("Turning Back")
                    j += 1

                if choice_4 == "go around":
                    print("going around")
                    j += 1

                if choice_4 == "go through":
                    print("waiting in traffic...")
                    print("Estimated wait time: ", s)
                    time.sleep(s)
                    j += 0
                    m += 50

        if Event == "Police":
            while j == 0:
                choice_4 = str(input("Would you turn back, go through, or go around?")).lower()
                if choice_4 == "turn back":
                    print ("Turning Back")
                    j += 1

                if choice_4 == "go around":
                    print ("going around")
                    j += 1

                if choice_4 == "go through":
                    print ("Going through")
                    choice_4a = str(input("The police officer sees you, and starts chasing you, would you pull over, or run")).lower()      
                    while j==0:
                        if choice_4a == "pull over":
                            print ("The police offiver asks for you Licence and Registration")
                            if a == 1:
                                print("You have a licence")
                                if b == 1:
                                        print("You have a registration")
                                        print("You are free to go!")
                                        j += 1

                                if a != 1 and b != 1:
                                        print("game over! You got arrested")
                                        j += 1
                                        h += 1
                                        k += 1

                            if a != 1 and b != 1:
                                    print("game over! Your arrested")
                                    j += 1
                                    h += 1
                                    k += 1

                            if choice_4a == "run": #Broken area of code

                                PoliceEvent = random.choice(RandEventPolice) #Printed RandEventPolice instead of choosing a string

                                #PoliceEvent didn't work
                                
                                if PoliceEvent == "Caught":
                                    print("Game Over, you got caught!")
                                    j += 1
                                    h += 1
                                    k += 1
                                
                                if PoliceEvent == "Escaped":
                                    print("You escaped!")
                                    j += 1
                            
        if Event == "Hitch-hiker":
            print("This event is coming soon")

        if Event == "Traffic":
            while j == 0:
                choice_4 = str(input("Would you turn back, go through, or go around?")).lower()
                if choice_4 == "turn back":
                    print ("Turning Back")
                    j += 1

                if choice_4 == "go through":
                    print ("Unable go through, try again")
                    j += 0

                if choice_4 == "go around":
                    print ("going around")
                    j += 1         

        if Event == "Nothing":
            print ("Nothing there carrying on")

        d += 1
        m += 10
                
                    
    if k == 1:
        choice_console = str(input("Do you want to play again??"))

        if choice_console == "yes":
            continue

        if choice_console == "no":
            print("Exiting...")
            time.sleep(1)








