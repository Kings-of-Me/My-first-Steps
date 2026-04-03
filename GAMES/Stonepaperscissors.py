from random import randint
from datetime import datetime

import time
t=["Stone","Paper","Scissor"]
filename="E:\Yuvaraj\GAME\data\SPS"
def result(c,p,T,n):
    print ("COMPUTER: %d" % c)
    print ("PLAYER  : %d" % p)
    print ("TIES    : %d" % T)
    print ("The Total Matchs is %d" % n)
    with open(filename,"a")as F:
        F.write(datetime.now().strftime("DATE:%d/%m%Y\nTIME%X\nCOMPUTER:{}\nPLAYER:{}\nTIES:{}\nTOTAL MATCHES:{}\n".format(c,p,T,n)))
    F.close()
    if p > c:
        print ("*-*-*-*-*-*-*-*-*YOU WON THE MATCH*-*-*-*-*-*-*-*-*-*-")
        with open(filename, "a")as F:
            F.write(datetime.now().strftime("PLAYER WON THE MATCH"))
        F.close()
    elif p == c:
        print ("*-*-*-*-*-*-*-*-*THE MATCH IS TIE*-*-*-*-*-*-*-*-*-*-*-")
        with open(filename, "a")as F:
            F.write(datetime.now().strftime("THE MATCH IS TIE"))
        F.close()
    else:
        print ("*-*-*-*-*-*-*-*-*YOU LOSE THE MATCH*-*-*-*-*-*-*-*-*-*-")
        with open(filename, "a")as F:
            F.write(datetime.now().strftime("PLAYER LOSE THE MATCH"))
        F.close()
        time.sleep(2)
    import menu
    menu.start()
def play():
    while True:
        try:
            WIN=input("Enter the Winning Point: ")
        except Exception as e:
            print ("ERROR:")
            continue
        break


    c=0
    p=0
    T=0
    n=0
    player=False
    computer=t[randint(0,2)]
    while player == False:
        player=input("\nStone Paper Scissor? ")
        n+=1
        print ("\nCOMPUTER: ", computer,"\n")
        if player==computer:
            print ("*  *   *  Tie *   *   *   *\n")
            T+=1
            print ("COMPUTER:PLAYER")
            print ("   %d   :  %d  \n" % (c,p))
        elif player == "Stone":
            if computer=="Paper":
                print ("*   *   *  You Lose *   *   * \n")
                c+=1
            else :
                print ("*   *   *  You Win *   *  *  \n")
                p+=1
            print ("COMPUTER:PLAYER")
            print ("   %d   :  %d  \n"%(c,p))
        elif player == "Paper":
            if computer=="Scissor":
                print ("*   *   *  You Lose *   *   * \n")
                c += 1
            else:
                print ("*   *   *  You Win *   *  *  \n")
                p += 1
            print ("COMPUTER:PLAYER")
            print ("   %d   :  %d  \n" % (c,p))
        elif player == "Scissor":
            if computer == "Stone":
                print ("*   *   *  You Lose *   *   * \n")
                c += 1
            else:
                print ("*   *   *  You Win *   *  *  \n")
                p += 1
            print ("COMPUTER:PLAYER")
            print ("   %d   :  %d  \n" % (c,p))
        elif player == "Result":
            result(c,p,T,n)
        else:
            print ("That is not Invalid , Check Your Spelling")
            n-=1

        if c==WIN or p==WIN:
            result(c,p,T,n)
        player = False
        computer = t[randint(0, 2)]