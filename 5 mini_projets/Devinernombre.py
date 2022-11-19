import random
chosed_number =random.randint(1,6)
from datetime import datetime
now = datetime.now()


for i in range(3):
    proposed_number =int(input("Type here the number you guessed"))
    if chosed_number==proposed_number:
       print(f" Congratulations, on {now}, you've done with success!")
       print(f"The right number is {chosed_number}")
       break
    elif chosed_number>proposed_number:
       print("Your guessed number is less than my chosed")
    elif chosed_number<proposed_number:
       print("Your number is greater than the one it should be (mine)")

else:
    print(f" On {now},You lost! The right number was {chosed_number}")
 
