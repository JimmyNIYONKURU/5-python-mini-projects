import random 
from datetime import datetime
now=datetime.now()
print("Continue till you get your password")
longpass=int(input("How long do you want your password to be? "))
v="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!$%&()*+,-./:;<=>?@[]^_`{|}"
password="".join(random.sample(v,longpass))
print(f"On {now} you get this password: {password}. Please keep it or change it if you want the one you will be able to memorize easily")
