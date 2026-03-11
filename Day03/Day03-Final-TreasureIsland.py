print('''
                                               .       .
                                                \     /
                                             ._  '   '  _.
                                               '  o@o  '
                                                 o@@@o
                                             .-'  o@o  '-.
                                                 .   .
                                                /     \\
                                               .       .

                         'Xx  xX*,
                      ,*xXXx_xXx
                        _xXXXXXxx*,
                      ,*XXx@x@Xx
                        X @|@@ `x
                        '  ||    '
                           ||
                           ||
                           ||
                           ||
                        /ssssssss.
                  /sssssssSSSSssssssssss.
    /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

# Palm tree or pond (death)
choice1 = input("You see a palm tree and a pond in the distance. which would you like to explore? (palm tree or pond) ")

if choice1.lower() == "palm tree":
    print('''                        'Xx  xX*,
                      ,*xXXx_xXx
                        _xXXXXXxx*,
                      ,*XXx@x@Xx
                        X @|@@ `x
                        '  ||    '
                           ||
                           ||
                           ||
                           ||''')
    # hole (death) or shack
    choice2 = input("You arrived at the palm tree and see a hole beneath the tree and a shack to the left. Do you explore the hole or the shack? ")
    if choice2.lower() == "shack":
        print("""                              _________________
       _                     /\                `.
     _( )                   /  \                 `._             _ _
    ( (  )                .__.'                     `-._        ( ( )
    (_  ))_    ,-.  . _ ,'/`._                          `--_,' (     )
    _((_)( )  (   )  `._,'____`--.._____________________,.-'/   (_ _) )
   ( ))|(_ ))(_(  ))   || |  |    |    |    |    |    |    |      |(( _)
  (( _)|  |     |      ||-|--|====|====|====|====|====|====|      |  |
    |  ______......----||_|  |    |    |    |    |    |    |----------''
 --'''': _:   _ :      `-.|`-|====|====|====|====|====|====|      :  :_
   (_)):(  ))( (  ))  ,': :`-|____|____|____|____|____|____|  ~  _:(   )
""")
        choice3 = input("Upon entering the shack, you find a room with three doors. Do you enter the red, green, or blue door? (red, green, or blue) ")
        if choice3 == "red":
            print('''''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''''')
            print("YOU WON! Congratulations, you found the treasure!.")
        else:
            print("GAME OVER! You fell into a trap and died.")
    elif choice2.lower() == "hole":
        print("GAME OVER! When exploring the hole, your feet slipped and you fell all the way to the bottom. You died.")
elif choice1.lower() == "pond":
    print("GAME OVER! The pond turned out to be a mirage and it suddenly occured to you how thirsty you were. You died of thirst.")
else:
    print("Enter either palm tree or pond")