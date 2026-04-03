from GAMES import cri,Stonepaperscissors,guess
import time
filename1="E:\Yuvaraj\GAME\data\Cricket Mark"
filename2="E:\Yuvaraj\GAME\data\guess"
filename3="E:\Yuvaraj\GAME\data\SPS"
def read():
    while True:
        print ("Your Options are:-")
        time.sleep(0.5)
        print ("1.Cricket")
        time.sleep(0.5)
        print ("2.Guess")
        time.sleep(0.5)
        print ("3.Stone Paper Scissor")
        time.sleep(0.5)
        print ("4.Return to menu")
        time.sleep(0.5)
        opt=input("Enter your Option: ")
        if opt=="1":
            print()
            with open(filename1,"r")as f:
                print (f.read())
                f.close()
            time.sleep(5)
        elif opt=="2":
            print ()
            with open(filename2,"r")as f:
                print (f.read())
                f.close()
            time.sleep(5)
        elif opt=="3":
            print ()
            with open(filename3,"r")as f:
                print (f.read())
                f.close()
            time.sleep(5)
        elif opt=="4":
            return
        else :
            print ("Invalid Option")

def start():
    print ("                         Welcome   to   GAME   FILE")
    while True:
        print ("Your Options are:-")
        time.sleep(0.5)
        print ("1.CRICKET")
        time.sleep(0.5)
        print ("2.GUESS THE NUMBER")
        time.sleep(0.5)
        print ("3.STONE PAPER SCISSOR")
        time.sleep(0.5)
        print ("4.READ")
        time.sleep(0.5)
        print ("5.EXIT")
        time.sleep(0.5)
        opt=input("Enter your Option :   ")
        if opt=="1":
            cri.play()
        elif opt=="2":
            guess.play()
        elif opt=="3":
            Stonepaperscissors.play()
        elif opt=="4":
            read()
        elif opt=="5":
            exit()
        else :
            print ("Invalid Option")
