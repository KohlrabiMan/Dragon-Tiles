# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 11:02:18 2016

@author: rutherfordw & holbertjo

"""
import random                                                                 # import random



 
class Dragon_Tiles (object):
    
    def __init__(self):
        #items#
        self.Head1=0                                                          # Red Mage's head storage (max of 3 )
        self.Head2=0                                                          # Blue Mage's head storage (max of 3)
        self.Body1=0                                                          # Red Mage's body storage (max of 3)
        self.Body2=0                                                          # Blue Mage's body storage (max of 3)
        self.Tail1=0                                                          # Red Mage's tail storage (max of 3)
        self.Tail2=0                                                          # Blue Mage's tail storage (max of 3)
        #current dragons#
        self.D1=""                                                            # Red Mage's current dragon type
        self.D2=""                                                            # Blue Mage's current dragon type
        #Player stats#
        self.Health1=3                                                        # Red Mage's health     
        self.Health2=3                                                        # Blue Mage's health
        self.Graveyard1=0                                                     # Red Mage's # of dead dragons (lose=5)
        self.Graveyard2=0                                                     # Blue Mage's # of dead dragons (lose=5)
        #used elements#
        self.Fire1=False                                                      # Red Mage has conjured a fire dragon
        self.Fire2=False                                                      # Blue Mage has conjured a fire drgon
        self.Earth1=False                                                     # Red Mage has conjured a earth dragon
        self.Earth2=False                                                     # Blue Mage has conjured a earth dragon
        self.Water1=False                                                     # Red Mage has conjured a water dragon
        self.Water2=False                                                     # Blue Mage has conjured a water dragon
        self.Wind1=False                                                      # Red Mage has conjured a wind dragon
        self.Wind2=False                                                      # Blue Mage has conjured a wind dragon
        self.Metal1=False                                                     # Red Mage has conjured a metal dragon
        self.Metal2=False                                                     # Blue Mage has conjured a metal dragon  
       
    def Turn_Giver(self):
        '''Pre: none
        Post: Which player is which mage.'''
        Coin =random.randint(1,2)                                             # random number generator of 1 or 2
        
        if Coin==1:
            print "\n" + "*You are Red Mage!*" + "\n"                         # Player 1
        else:
            print "\n" + "*You are Blue Mage!*" + "\n"                        # Player 2
        
    def Player1_Turn(self):
        '''Pre: self.Head1&2, self.Body1&2, self.Tail1&2
        Post: Acquires items based upon die roll.'''
        Dragon_Die=random.randint(1,3)                                        # random number generator of 1-3
        Player1_Prompt=raw_input("Press enter to roll dragon die: ")          # roll prompt
        if Player1_Prompt=="" and self.D1=="":                                # Player 1 inputs enter to roll
            if Dragon_Die == 1 and self.Head1<=2:                             # if Player 1 rolls a 1
                self.Head1 += 1                                               # acquire 1 head
                print "\n" + "*Red Mage,head aquired*" + "\n"                 # notes what part was acquired   
            
            elif Dragon_Die == 2 and self.Body1<=2:                           # if Player 1 rolls a 2
                self.Body1 += 1                                               # acquire 1 body
                print "\n" + "*Red Mage,body aquired*" + "\n"                 # notes what part was acquired
          
            elif Dragon_Die == 3 and self.Tail1<=2:                           # if player 1 rolls a 3
                self.Tail1 += 1                                               # acquire 1 tail
                print "\n" + "*Red Mage,tail acquired*" + "\n"                # notes what part was acquired
#######################################################################################################################        
            #limit reached clause
            elif Dragon_Die == 1 and self.Head1==3 :                          # if Player 1 rolls a 1 and has 3 heads
                print "\n" + "*Red Mage,head limit reached,reroll.*" + "\n"   # notes limitation reached, reroll
                self.Player1_Turn()                                           # recursion call
            
            elif Dragon_Die == 2 and self.Body1==3:                           # if Player 1 rolls a 2 and has 3 bodies
               print "\n" + "*Red Mage,body limit reached,reroll.*" + "\n"    # notes limitation reached, reroll
               self.Player1_Turn()                                            # recursion call
          
            elif Dragon_Die == 3 and self.Tail1==3:                           # if Player 1 rolls a 3 and has 3 tails
                print "\n" + "*Red Mage,tail limit reached,reroll.*" + "\n"   # notes limitation reached, reroll
                self.Player1_Turn()                                           # recursion call
#######################################################################################################################
        # skip clause
        elif self.D1!="":                                                     # if Player 1 currently has a dragon
            print "\n" + "*Red Mage dragon active, turn skipped*" + "\n"      # turn skipped
            
                 
      
                 
    def Dragon_Conjure1(self):
        '''Pre: items(P1), self.D1, and used elements(P1)
        Post: Once player 1 has one of each item conjure a dragon based upon die roll.'''
        Element_Die=random.randint(1,5)                                       # random number generator 1-5
        if self.D1=="":                                                       # if Player 1 does not have a dragon  
            if self.Head1>=1 and self.Body1>=1 and self.Tail1>=1:             # and if a Player 1 has 1 of each item
                self.Head1 += -1                                     
                self.Body1 += -1                                              #} remove 1 of each item from storage
                self.Tail1 += -1
                print "*Red Mage dragon conjuring...*" + "\n"                 # conjure pending 
               
                if Element_Die == 1 and self.Fire1==False:                    # if Player 1 rolls x and has not used x
                    self.Fire1=True                                           # set x to used
                    self.D1="F"                                               # set current dragon to x
                    print "**Red Mage,Fire dragon conjured.**" + "\n"         # x is conjured
                    
                elif Element_Die == 2 and self.Earth1==False:                 # see lines 91-94 for lines 96-115
                    self.Earth1=True
                    self.D1="E"
                    print "**Red Mage,Earth dragon conjured.**" + "\n"
                    
                    
                elif Element_Die == 3 and self.Water1==False:
                    self.Water1=True
                    self.D1="H2O"
                    print "**Red Mage,Water dragon conjured.**" + "\n"
                    
                elif Element_Die == 4 and self.Wind1==False:
                    self.Wind1=True
                    self.D1="W"
                    print "**Red Mage,Wind dragon conjured.**" + "\n"
                    
                elif Element_Die == 5 and self.Metal1==False:
                    self.Metal1=True
                    self.D1="M"
                    print "**Red Mage,Metal dragon conjured.**" +  "\n"
#######################################################################################################################
                # reconjure clause
                elif Element_Die == 1 and self.Fire1==True:                   # if Player 1 rolls x and has used x
                    print "**Conjure failed, reconjuring.**" + "\n"           # reconjure
                    self.Dragon_Conjure1()                                    # recursion call
                    
                elif Element_Die == 2 and self.Earth1==True:                  # see lines 118-120 for lines 122-138
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure1()
                    
                    
                elif Element_Die == 3 and self.Water1==True:
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure1()
                    
                elif Element_Die == 4 and self.Wind1==True:
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure1()
                    
                elif Element_Die == 5 and self.Metal1==True:
                    print "**Conjure failed, reconjuring.**" +  "\n"
                    self.Dragon_Conjure1()
                
            
            
            
    def Player2_Turn(self):
        '''see Player1_Turn. applies to Player 2'''
        Dragon_Die=random.randint(1,3)                                        # see Player1_Turn function
        Player2_Prompt=raw_input("Press enter to roll dragon die: ")          # applies to player 2
        if Player2_Prompt=="" and self.D2=="":                                
            if Dragon_Die == 1 and self.Head2<=2:
                self.Head2 += 1
                print "\n" + "*Blue Mage,head aquired.*" + "\n"               
            
            elif Dragon_Die == 2 and self.Body2<=2:
                self.Body2 += 1
                print "\n" + "*Blue Mage,body aquired.*" + "\n"               
          
            elif Dragon_Die == 3 and self.Tail2<=2:
                self.Tail2 += 1
                print "\n" + "*Blue Mage,tail acquired.*" + "\n"              
#######################################################################################################################        
            elif Dragon_Die == 1 and self.Head2==3 :
                print "\n" + "*Blue Mage,head limit reached,reroll.*" + "\n"  
                self.Player2_Turn()                                           
            
            elif Dragon_Die == 2 and self.Body2==3:
               print "\n" + "*Blue Mage,body limit reached,reroll.*" + "\n"   
               self.Player2_Turn()                                            
          
            elif Dragon_Die == 3 and self.Tail2==3:
                print "\n" + "*Blue Mage,tail limit reached,reroll.*" + "\n"  
                self.Player2_Turn()                                           
#######################################################################################################################
        elif self.D2!="":
            print "\n" + "*Blue Mage dragon active, turn skipped*" + "\n"
                
            
        
    def Dragon_Conjure2(self):
        '''see Dragon_Conjure2, applies to Player 2'''                                        
        Element_Die=random.randint(1,5)                                       # see Dragon_Conjure1 function
        if self.D2 =="":                                                      # applies to Player 2
            if self.Head2>=1 and self.Body2>=1 and self.Tail2>=1:
                self.Head2 += -1
                self.Body2 += -1
                self.Tail2 += -1
                print "*Blue Mage dragon conjuring...*" + "\n"
    
                if Element_Die == 1 and self.Fire2==False:
                    self.Fire2=True
                    self.D2="F"
                    print "**Blue Mage,Fire dragon conjured.**" + "\n"
                    
                elif Element_Die == 2 and self.Earth2==False:
                    self.Earth2=True
                    self.D2="E"
                    print "**Blue Mage,Earth dragon conjured.**" + "\n"
                    
                elif Element_Die == 3 and self.Water2==False:
                    self.Water2=True
                    self.D2="H2O"
                    print "**Blue Mage,Water dragon conjured.**" + "\n"
                    
                elif Element_Die == 4 and self.Wind2==False:
                    self.Wind2=True
                    self.D2="W"
                    print "**Blue Mage,Wind dragon conjured.**" + "\n"
                    
                elif Element_Die == 5 and self.Metal2==False:
                    self.Metal2=True
                    self.D2="M"
                    print "**Blue Mage,Metal dragon conjured.**" + "\n"
#######################################################################################################################
                elif Element_Die == 1 and self.Fire2==True:
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure2()
                    
                elif Element_Die == 2 and self.Earth2==True:
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure2()
                    
                    
                elif Element_Die == 3 and self.Water2==True:
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure2()
                    
                elif Element_Die == 4 and self.Wind2==True:
                    print "**Conjure failed, reconjuring.**" + "\n"
                    self.Dragon_Conjure2()
                    
                elif Element_Die == 5 and self.Metal2==True:
                    print "**Conjure failed, reconjuring.**" +  "\n"
                    self.Dragon_Conjure2()
                

            
    def Battle(self):
        '''Pre: current dragons and player stats
        Post: if a dragon is present battle occurs leading to (a) slain dragon(s) or damage to a player.'''
        if self.D1 != "" and self.D2 != "":                                   # if both players have a dragon
            if self.D1=="F" and self.D2=="W" or self.D1=="F" and self.D2=="M": # if x vs x or x vs y
                self.D2=""                                                     # Player 2 no longer has a dragon
                print "***Blue Mage's dragon slain!***" + "\n"                 # Player 2's dragon slain
                self.Graveyard2 += 1                                           # add 1 to Player 2's graveyard
            
            elif self.D1=="E" and self.D2=="F" or self.D1=="E" and self.D2=="H2O":
                self.D2=""                                                  
                print "***Blue Mage's dragon slain!***" + "\n"                 # see lines 234-237 for lines 239-257
                self.Graveyard2 +=1
            
            elif self.D1=="H2O" and self.D2=="F" or self.D1=="H2O" and self.D2=="M":
                self.D2=""
                print "***Blue Mage's dragon slain!***" + "\n"
                self.Graveyard2 +=1
            
            elif self.D1=="W" and self.D2=="H2O" or self.D1=="W" and self.D2=="E":
                self.D2=""
                print "***Blue Mage's dragon slain!***" + "\n"
                self.Graveyard2 +=1
           
            elif self.D1=="M" and self.D2=="W" or self.D1=="M" and self.D2=="E":
                self.D2=""
                print "***Blue Mage's dragon slain!***" + "\n"
                self.Graveyard2 +=1
#######################################################################################################################
            # Player 1 battle lose clause
            elif self.D2=="F" and self.D1=="W" or self.D2=="F" and self.D1=="M":
                self.D1=""                                                      # see lines 234-257 for lines 260-283
                print "***Red Mages's dragon slain!***" + "\n"
                self.Graveyard1 += 1
            
            elif self.D2=="E" and self.D1=="F" or self.D2=="E" and self.D1=="H2O":
                self.D1=""
                print "***Red Mages's dragon slain!***" + "\n"
                self.Graveyard1 +=1
            
            elif self.D2=="H2O" and self.D1=="F" or self.D2=="H20" and self.D1=="M":
                self.D1=""
                print "***Red Mage's dragon slain!***" + "\n"
                self.Graveyard1 +=1
            
            elif self.D2=="W" and self.D1=="H2O" or self.D2=="W" and self.D1=="E":
                self.D1=""
                print "***Red Mage's dragon slain! Dragon enters Player 1's graveyard.***" + "\n"
                self.Graveyard1 +=1
           
            elif self.D2=="M" and self.D1=="W" or self.D2=="M" and self.D1=="E":
                self.D1=""
                print "***Red Mage's dragon slain! Dragon enters Player 1's graveyard.***" + "\n"
                self.Graveyard1 +=1
#######################################################################################################################
            # tie clause                       #line below: should a dragon battle a dragon of the same type
            elif self.D1=="F" and self.D2=="F" or self.D1=="H2O" and self.D2=="H2O" or self.D1=="W" and self.D2=="W" or self.D1=="E" and self.D2=="E" or self.D1=="M" and self.D2=="M":
                 self.D1=""                                 #} both players no longer have a dragon
                 self.D2=""                                 
                 print "***The dragons are evenly matched and slay one another!***" + "\n" #both dragons slain
                 self.Graveyard1 += 1                       #} both players add 1 to their graveyards
                 self.Graveyard2 += 1
######################################################################################################################            
        # damage clause
        elif self.D1 != "" or self.D2 != "":                      # if one player has a dragon and the other does not
            if self.D1!="" and self.D2=="":                       #  if Player 1 has a dragon and Player 2 does not      
                self.Health2 += -1                                # remove 1 from Player 2's health. Player 2 damaged
                print "***Direct hit! Blue Mage damaged! " + str(self.Health2) + " health remaining.***" "\n" 
            
            elif self.D2!="" and self.D1=="":                     # if Player 2 has a dragon and Player 1 does not
                self.Health1 += -1                                # remove 1 from Player 1's health. Player 1 damaged
                print "***Direct hit! Red Mage damaged! " + str(self.Health1) + " health remaining.***" "\n"

    def main(self):
        '''Pre: initializer
        Post: driver function'''
        Game= Dragon_Tiles()                                                  # class variable
        Game_Prompt = raw_input("Start Game Press Enter:")                    # starting prompt
        if Game_Prompt == "":                                                 # input enter to proceed
            Game.Turn_Giver()                                                 # call Turn_Giver
            while Game.Health1!=0 and Game.Health2!=0 and Game.Graveyard1!=5 and Game.Graveyard2!=5: # both players have yet to reach 0 health and both still have dragons to be used 
                print "Red Mage turn commence" + "\n"                         # Player 1 turn commence 
                Game.Player1_Turn()                                           # call Player1_Turn
                Game.Dragon_Conjure1()                                        # call Dragon_Conjure1
                print "Blue Mage turn commence" + "\n"                        # Player 2 turn commence 
                Game.Player2_Turn()                                           # call Player2_Turn 
                Game.Dragon_Conjure2()                                        # call Dragon_Conjure2
                Game.Battle()                                                 # call Battle 
            
            if Game.Health1<=0 or Game.Graveyard1>=5:                  # if Player 1 has no health or a full graveyard
                print "****RED MAGE VANQUISHED!****"                   # Player 1 vanquished 
                
            elif Game.Health2<=0 or Game.Graveyard2>=5:                # if Player 2 has no health or a full graveyard
                print "****BLUE MAGE VANQUISHED!****"                  # Player 1 vanquished
                
            elif Game.Graveyard1==5 and Game.Graveyard2==5:     # if both players reach full graveyards simultaneously
                if Game.Health1 > Game.Health2:                 # if Player 1 has more health
                    print "****BLUE MAGE VANQUISHED!****"       # Player 2 vanquished
                    
                elif Game.Health1 < Game.Health2:               # if Player 2 has more health
                    print "****RED MAGE VANQUISHED!****"        # Player 1 vanquished
                    
                elif Game.Health1 == Game.Health2:              # if both Players have the same health
                    print "***THE MAGES ARE EVENLY MATCHED. BOTH MAGES VANQUISH EACH OTHER!***"    # Players 1&2 tie
                
                
                
                
if __name__ == '__main__':            # calls main
    objName = Dragon_Tiles()          
    objName.main()                    
               
        