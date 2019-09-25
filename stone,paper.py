#   WAP to make game of stone paper and scissor
def menu():      # Function to define menu
     print("enter 1 to select stone")
     print("enter 2 to select paper")
     print("enter 3 to select scissor")

def score():   # function to print and check score
    print(" .................SCORES.................")
    print("user:",user)
    print("computer:",computer)
    #condition if score of user or computer is 5 check and print corresponding output
    
       
# main body of program     
print(" WELCOME TO PLAY STONE/PAPER/SCISSOR")
print("stone will beat scissor")
print("scissor will beat paper")
print("paper will beat stone")
a= int(input("Enter 1 to play: "))  # to give input if we want to play
if(a==1):   # if user entered 1 to play
     
 user=0                  # score of user=0
 computer=0              # score of computer=0
 choice=True             # making choice= true for while loop
 while(choice):
       if(user==5 or computer==5):                        # checking if the score of user or computer is 5
         if(user==5 and user>computer):                   # if score of anyone of them is 5 print the required statement and make choice= false 
           print("YOU WON!!! CONGRATULATIONS")     
         else:
           print("I WON!!! Better luck next time")      
         choice=False
       else:
         menu()               # calling function menu
         ch= int(input())     # taking choice from the user
         from random import randint
         c=randint(1,3)       # taking random no from the computer from 1 to 3
         if(ch==c):
          print("no win no loss")            # if the choice of user and computer are same then the round will be won by none
          score()
         elif((ch==1 and c==3)):
          print("   I choose scissor  ")    # if user choose stone and computer choose scissor then user will win
          print(" uggh!! I lost this round")
          user=user+1
          score()
         elif((ch==3 and c==2)):            # if user choose scissor and computer choose paper then user will win
          print("   I choose paper  ")
          print(" uggh!! I lost this round")
          user=user+1
          score()
         elif((ch==2 and c==3)):           # if user choose paper and computer choose scissor then computer will win
          print("I choose scissor")
          print("Yes I won this round")
          computer=computer+1
          score()
         elif((ch==1 and c==2)):           # if user choose stone and computer choose paper then computer will win
          print("I choose paper")
          print("Yes I won this round")
          computer=computer+1
          score()
         elif((ch==2 and c==1)):          # if user choose paper and computer choose stone user will win
          print("   I choose stone ")
          print(" uggh!! I lost this round")
          user=user+1
          score()
         elif((ch==3 and c==1)):         # if user choose scissor and computer choose stonethen computer will win
          print("I choose stone")
          print("Yes I won this round")
          computer=computer+1
          score()     
         else:
          d=input("do you want to exit??(Y/N)")   # if the user do not input correct choice and then if he wants to exit the game
          if(d=="y"):                              # if yes then say bye and make your choice false
            print("BYE BYE")
          choice=False

   
 


 
    
         

   


      
    
            
    
      
        
        
        
