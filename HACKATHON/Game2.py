def ropasci():
    score1 = 0
    score2 = 0
    while True:
        you = input("Enter rock paper or scissors. Enter stop to stop playing: \n")
        import random
        other = random.randint(1,3)
        if other == 1:
            choice = "rock"
        elif other == 2:
            choice = "paper"
        elif other == 3:
            choice = "scissors"
        
        if you=="rock" and other == 1:
            print("player 1:",you," player 2:",choice)
            print("Tie!")
        elif you=="rock" and other == 2:
            print("player 1:",you," player 2:",choice)
            print("You Lose!")
            score2+=1
        elif you=="rock" and other == 3:
            print("player 1:",you," player 2:",choice)
            print("You Win!")
            score1+=1
            
        elif you=="paper" and other == 1:
            print("player 1:",you," player 2:",choice)
            print("You Win!")
            score1+=1
        elif you=="paper" and other == 2:
            print("player 1:",you," player 2:",choice)
            print("Tie!")    
        elif you=="paper" and other == 3:
            print("player 1:",you," player 2:",choice)
            print("You Lose!")
            score2+=1
        
        elif you=="scissors" and other == 1:
            print("player 1:",you," player 2:",choice)
            print("You Lose!")
            score2+=1
        elif you=="scissors" and other == 2:
            print("player 1:",you," player 2:",choice)
            print("You win!")
            score1+=1
        elif you=="scissors" and other == 3:
            print("player 1:",you," player 2:",choice)
            print("Tie!")
        elif you=="stop":
            print("Player 1:",score1,"points")
            print("Player 2:",score2,"points")
            if score1>score2:
                print("You win!")
            elif score2>score1:
                print("You lose!")
            else:
                print("Tie!")
            break
        


        
