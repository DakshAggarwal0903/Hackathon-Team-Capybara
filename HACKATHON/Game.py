def randnum():
    while True:
        import random
        num = random.randint(1,15)
        for i in range(0,3):
            score = 0
            a = int(input("Enter a number between 1 and 15: "))
            if a == num:
                print("You win!")
                score+=1
                break
            elif a>num:
                print("Too high")
            else:
                print("Too low")
        if score == 1:
            print("Well done")
        else:
            print("You lose! Better luck next time")
        play = input("Do you want to keep playing?")
        if play=='yes':
            print("Ok")
        else:
            print("Ok")
            break
        
            
