# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:46:42 2019

@author: bruno
"""
import random 

userChoice = input("Choose \"r\" or \"p\" or \"s\"")
pcChoice = random.choice(["r","p","s"])


If (userChoice == "r") and (pcChoice == "r"):
    print("You choosed rocks! Computer choosed rocks! \n Its a tie!")
Elif (userChoice == "r") and (pcChoice == "p"):
    print("You choosed rocks! Computer choosed paper! \n You lost!")
Elif (userChoice == "r") and (pcChoice == "s"):
    print("You choosed rocks! Computer choosed scissors! \n You won!")
    
Elif (userChoice == "p") and (pcChoice == "r"):
    print("You choosed paper! Computer choosed rocks! \n You won!")
Elif (userChoice == "p") and (pcChoice == "p"):
    print("You choosed paper! Computer choosed paper! \n Its a tie!")
Elif (userChoice == "p") and (pcChoice == "s"):
    print("You choosed paper! Computer choosed scissors! \n You lost!")
    
Elif (userChoice == "s") and (pcChoice == "r"):
    print("You choosed rocks! Computer choosed rocks! \n You lost!")
Elif (userChoice == "s") and (pcChoice == "p"):
    print("You choosed rocks! Computer choosed paper! \n You won!")
Else """(userChoice == "s" and pcChoice == "s"):"""
    print("You choosed rocks! Computer choosed scissors! \n Its a tie!")
    
