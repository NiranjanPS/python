###############################################################################################################
## Console based Snake Ladder Game    #########################################################################
## Author : Niranjan P S              #########################################################################
## Date : 29-01-2019                  #########################################################################
###############################################################################################################

import random
import sys
class snake_ladder:
    
    def __init__(self):
        self.D = {0:0, 1:1, 2:2, 3:3, 4:18, 5:5, 6:6, 7:7, 8:15, 9:9, 10:2, 11:11, 12:22, 13:13, 14:14, 15:15, 16:16, 17:14, 18:18, 19:19, 20:6, 21:21, 22:22, 23:11, 24:24}
        self.disp = {0:'0', 1:'1', 2:'2', 3:'3', 4:'UP to 18', 5:'5', 6:'6', 7:'7', 8:'UP to 15', 9:'9', 10:'Down to 2', 11:'11', 12:'UP to 22', 13:'13', 14:'14', 15:'15', 16:'16', 17:'Down to 14',
                     18:'18', 19:'19', 20:'Down to 6', 21:'21', 22:'22', 23:'Down to 11', 24:'24'}
        self.row = []
        self.A =["hh", 0]
        self.B =["jj", 0]
        self.AB = [self.A[1], self.B[1]]
        self.count = [0, 0]
        self.state = 0
        self.r = 0
        self.playc = [3, 2, 4, 2,4,2,4,2,4,2,5,2,5,2,2,2,2,2,2,2,2]
        self.i = 0
        self.j = 0
        #print(self.A[0])
        #print(self.A[1])
        #print(self.B[0])
        #print(self.B[1])
        #print(self.AB)
        
    def game_start(self):
        sn.get_user_names()
        sn.say_hi()        
        sn.start_stop()
        sn.loop()
        sn.display_game()
    def update(self):
        print(("You got %d"%self.r))
        print(("before AB:  %d"%self.AB[self.state]))
        self.AB[self.state] = self.AB[self.state] + self.r
        if self.AB[self.state] < 25:
            self.AB[self.state] = self.AB[self.state]
            #self.A[1] = self.AB[0]
            #self.B[1] = self.AB[1]
        else:
            self.AB[self.state] = self.AB[self.state] - self.r
        print(("After AB:  %d"%self.AB[self.state]))
        

    def update_position(self):
        self.A[1] = self.D[self.AB[0]]
        self.B[1] = self.D[self.AB[1]]
        
    def toggle(self):
        if (self.state == 0):
            self.state = 1
            
        else:
            self.state = 0
        self.AB[1] = self.B[1]
        self.AB[0] = self.A[1]

    def display_turn(self):
        if self.state == 0:
            print(("------------------------------Now %10s's Turn-----------------------------"%self.A[0]))
        else:
            print(("------------------------------Now %10s's Turn-----------------------------"%self.B[0]))

    def play(self):
        #print("i before",self.i)
        self.r = random.randint(1,6)#self.playc[self.i]
        
        #print("r ",self.r)
        #self.i = self.i + 1 #random.randint(1,6)
        #print("i after ",self.i)
    def loop(self):
        self.display_game()
        while ((self.A[1]!=24) and (self.B[1]!=24)):
            print("--------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------")
            
            self.display_turn()
            print(("before A: %d"%self.A[1]))
            print(("before B: %d"%self.B[1]))

            #print("stop")           
            self.key_input()
            self.play()
            # print(self.r)
            
            self.update()
            self.update_position()
            print(("After A: %d"%self.A[1]))
            print(("After B: %d"%self.B[1]))
                      
            if self.r == 6:
                self.r = self.r
            else:
                self.count[self.state] = self.count[self.state] + 1
                self.toggle()
            self.AB[1] = self.B[1]
            self.AB[0] = self.A[1]
            self.display_game()
                
        self.display_winner()

    def display_winner(self):
        print("--------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------")
        if self.A[1] == 24:
            print(("_____________________________%s won the game in %d turns____________________________"%(self.A[0],self.count[0])))
        elif self.B[1] == 24:
            print(("_____________________________%s won the game in %d turns____________________________"%(self.B[0],self.count[1])))
        print("--------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------\n\n")
        self.a = input("Press any key to exit")
        sys.exit(0)
        
    def display_game(self): 
        del self.row[:]
        print("-----------------------------SNAKE and LADDER Game------------------------------\n")
        for key, val in sorted(self.disp.items()):
            if ((self.A[1] == key) or (self.B[1] == key)):
                if ((self.A[1] == key) and (self.B[1] == key)):
                    self.row.append(self.A[0] + ", " + self.B[0])
                else:
                    if (self.A[1] == key):
                        self.row.append(self.A[0])
                    if (self.B[1] == key):
                        self.row.append(self.B[0])
                    
            else:
                self.row.append(val)
            #print(key)
            #print(self.row)
        
        print(("%15s %15s %15s %15s %15s"%(self.row[20],self.row[21],self.row[22],self.row[23],self.row[24])))
        print(("%15s %15s %15s %15s %15s"%(self.row[19],self.row[18],self.row[17],self.row[16],self.row[15])))
        print(("%15s %15s %15s %15s %15s"%(self.row[10],self.row[11],self.row[12],self.row[13],self.row[14])))
        print(("%15s %15s %15s %15s %15s"%(self.row[9],self.row[8],self.row[7],self.row[6],self.row[5])))
        print(("%15s %15s %15s %15s %15s"%(self.row[0],self.row[1],self.row[2],self.row[3],self.row[4])))
    def get_user_names(self):
        self.A[0] = input("Enter player A name:      ")
        self.B[0] = input("Enter player B name:      ")
        
        
    def say_hi(self):
        print(("\nHi %s and %s \n" %(self.A[0], self.B[0])))
        print("------------------------Welcome to Snake and Ladder game------------------------\n")
        #print(self.A[0])
        #print(self.A[1])
        #print(self.B[0])
        #print(self.B[1])
        
    def start_stop(self):
        self.key = input("________________________Enter S for Start and Q for quit________________________\n")
        if ((self.key == 'S') or (self.key == 's')):
            print("______________________________Game starts here_________________________________\n")
            #self.key_input()
        elif ((self.key == 'Q') or (self.key == 'q')):
            print("_____________________________________Game Ends here____________________________________\n")
            #self.start_stop()
            sys.exit(0)
        else:
            print("_____________________________________Enter valid KEY____________________________________\n")
            self.start_stop()

    def resume(self):
        self.key = input()
        if ((self.key == 'r') or (self.key == 'R')):
            pass
        else:
            self.resume()
    def key_input(self):
        self.key = input()
        if ((self.key == 'q') or (self.key == 'Q')):
            print("_____________________________________Game Ends here____________________________________\n")
            sys.exit(0)
        elif ((self.key == 'p') or (self.key == 'P')):
            print("___________________Game is paused to resume press R or r _______________________\n")
            self.resume()
            self.display_turn()
            self.key_input()
        elif (((self.key == 'a') or (self.key == 'A')) and (self.state == 0)):
            pass
        elif (((self.key == 'b') or (self.key == 'B')) and (self.state == 1)):
            pass
        elif ((self.key == 'a') or (self.key == 'A') or (self.key == 'b') or (self.key == 'B')):
            print("_________________________________Wrong person played_____________________________________\n")
            self.key_input()
        else:
            print("____________________________________Enter valid KEY______________________________________\n")
            self.key_input()
        
sn = snake_ladder()
sn.game_start()

