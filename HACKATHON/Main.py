import Game
import Game2
import Game3
import jokes
import reminder
import time as tm
import random as r

print("Hello, I am Synthia. I can play games, tell you jokes, and even set reminders for you.")

print("""Options-
1. Games
2. Jokes
3. Reminders \n""")
tm.sleep(2)
opt=input("Which of these would you like to do? \n")
if opt == "1":
    print("""GAMES-
1. Number guessing
2. Rock, Paper, Scissors
3. Mad Libs \n""")
    gameopt = input("Which of these would you like to do? \n")
    if gameopt == "1":
        Game.randnum()
    elif gameopt == "2":
        Game2.ropasci()
    elif gameopt == "3":
        Game3.madlib()
elif opt=="2":
    while True:
        num= r.randint(0,14)
        j,a= jokes(num)
        print(j)
        tm.sleep(2.5)
        print(a)
        tm.sleep(2.5)
        ans= input("\nDo you to hear another joke? Yes or No\n")
        if ans.lower()=="yes":
            pass
        elif ans.lower()=="no":
            print("Thanks for using the joke skill")
            break
        else:
            print("Invalid answer\n")
elif opt == "3":
    reminder.reminder()
else:
    print("Invalid Option")
