filename="E:\Yuvaraj\GAME\data\guess"


def play():
    name=input("What is Your name?  ")
    while True:
        from random import randint
        number=randint(1,10)
        print()
        nog=0
        print ("Okay %s I am Guessing a number between 1 to 10: \n"%name)
        while nog < 5:
            guess=int(input("Guess that number:  "))
            nog+=1
            if guess > number:
                print ("\nYour guess is too high")
            elif guess < number:
                print ("\nYour guess is too low")
            elif guess==number:
                break
        if guess==number :
            print ("\nYou find out the number within %d times"%nog)
            with open(filename,"a")as f:
                from datetime import datetime
                f.write(datetime.now().strftime("DATE:%d/%m/%Y\nTIME:%X\n{} find out the number within {} times\n".format(name,nog)))
            f.close()
        else:
            print ("\nYou did not findout the number and the number is %d"%number)
            with open(filename,"a")as f:
                from datetime import datetime
                f.write(datetime.now().strftime("DATE:%d%m%Y\nTIME:%X\n{} did not findout the number and the number is {}".format(name,number)))
            f.close()
        a=input("\nDo you want to again? (y/n)  :")
        if a=="y" or a=="Y":
            continue
        else :
            return