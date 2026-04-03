from random import randint

b = [0, 1, 2, 3, 4, 5, 6]
t = ["HEAD", "TAIL"]
bb = ["Batting", "Bouling"]
T = t[randint(0, 1)]
from datetime import datetime

filename = ".\data\Cricket Mark"


def result(p, c):
    print("\n")
    print ("MARKS:-")
    print ("COMPUTER:%d" % c)
    print ("PLAYER  :%d" % p)
    if p > c:
        print ("""             ***                 ***          ***       ***      ***
              ***               ***        ***   ***    *****    ***
               ***     ***     ***        ***     ***   *** **   ***
                ***   *****   ***         ***     ***   ***  **  ***
                 *** *** *** ***          ***     ***   ***   ** ***
                  *****   *****            ***   ***    ***    *****
                   ***     ***                ***       ***     ****""")
        with open(filename, "a") as f:
            f.write(datetime.now().strftime(
                "DATE:%d/%m/%Y\nTIME:%X\nCOMPUTER:{}\nPLAYER  :{}\nBOULINGBALLS:{}\nBATTINGBALLS:{}\n     PLAYER WON THE MATCH \n\n".format(c, p,bo,ba)))
            f.close()
    elif p == c:
        print ("""        *********************   *********************    *************
        *********************   *********************    *************
                *****                   *****            ***
                *****                   *****            *************
                *****                   *****            *************
                *****                   *****            ***
                *****           *********************    *************
                *****           *********************    *************""")
        with open(filename, "a") as f:
            f.write(datetime.now().strftime(
                "DATE:%d/%m/%Y\nTIME:%X\nCOMPUTER:{}\nPLAYER  :{}\nBOULINGBALLS:{}\nBATTINGBALLS:{}\n     THE MATCH IS TIE \n\n".format(c, p,bo,ba)))
            f.close()
    else:
        print ("""   ****               ****         ******************      ****************
   ****             ********       ******************      ****************
   ****           ****    ****     ****                    ****
   ****          ****      ****    ****                    ****
   ****          ****      ****    ******************      ****************
   ****          ****      ****    ******************      ****************
   ****          ****      ****                  ****      ****
   ****           ****    ****                   ****      ****
   ************     ********       ******************      ****************
   ************       ****         ******************      **************** """)
        with open(filename, "a") as f:
            f.write(datetime.now().strftime(
                "DATE:%d/%m/%Y\nTIME:%X\nCOMPUTER:{}\nPLAYER  :{}\nBOULINGBALLS:{}\nBATTINGBALLS:{}\n     PLAYER LOSE THE MATCH \n\n".format(c, p,bo,ba)))
            f.close()
    opt = input("Do You want to play again? (Y/N) : ")
    if opt == 'Y':
        play()
    else:
        import menu
        menu.start()


def win(BA, BO):
    if ba == 0 or bo == 0:
        print
    if ba!=0 and bo!=0 and ba>bo:
        result(P,C)
    if BA == 0 or BO == 0:
        return
    elif BA > BO:
        result(P, C)





def play():
    while True:
        global P
        P = 0
        global C
        C = 0
        global ba
        ba = 0
        global bo
        bo = 0

        playertoss = input("HEAD OR TAIL? ")
        print ("TOSS: "), T
        if playertoss == T:
            BB = input("Batting or Bouling? ")
            if BB == "Batting":
                print ("PLAYER : "), BB
                print ("PLAYER:BATTING")
                while True:
                    bo += 1
                    win(P, C)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo-=1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", P)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            P += player

                    except Exception as e:
                        print ("ERROR"),

                print ("PLAYER:BOULING")
                while True:
                    ba+=1
                    win(C, P)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", C)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            C += computer

                    except Exception as e:
                        print ("ERROR"),

                result(P, C)
                break
            else:
                print ("PLAYER : "), BB
                print ("PLAYER:BOULING")
                while True:
                    bo += 1
                    win(C, P)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", C)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            C += computer

                    except Exception as e:
                        print ("ERROR",)
                print ("PLAYER:BATTING")
                while True:
                    ba += 1
                    win(P, C)
                    try:
                        player = int (input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", P)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            P += player

                    except Exception as e:
                        print ("ERROR")
                result(P, C)
                break
        elif playertoss != T:
            BB = bb[randint(0, 1)]
            if BB == "Batting":
                print ("COMPUTER: ", BB)
                print ("PLAYER:BOULING")
                while True:
                    bo += 1
                    win(C, P)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", C)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            C += computer

                    except Exception as e:
                        print ("ERROR")
                print ("PLAYER:BATTING")
                while True:
                    ba += 1
                    win(P, C)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", P)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            P += player

                    except Exception as e:
                        print ("ERROR")
                result(P, C)
                break
            else:
                print ("COMPUTER: ", BB)
                print ("PLAYER:BATTING")
                while True:
                    bo += 1
                    win(P, C)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", P)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % bo)
                            P += player

                    except Exception as e:
                        print ("ERROR")
                print ("PLAYER:BOULING")
                while True:
                    ba += 1
                    win(C, P)
                    try:
                        player = int(input("Enter the number: "))
                        if player > 6:
                            print ("Number should be less than 6")
                            bo -= 1
                            continue
                        computer = b[randint(0, 6)]
                        if player == computer:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            print ("     *   *   *   *   *   * OUT   *   *   *   *   *   *   *")
                            print ("MARK:", C)
                            break
                        else:
                            print ("COMPUTER:%d" % computer)
                            print ("PLAYER  :%d" % player)
                            print ("BALLS   :%d" % ba)
                            C += computer

                    except Exception as e:
                        print ("ERROR",)
                result(P, C)
                break



