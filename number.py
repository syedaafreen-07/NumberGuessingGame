import random

steps=0
rand=random.randint(0,100)
while True:
    num=int(input("Enter the Number"))
    steps+=1
    if num>rand:
        print("Guees is High")
    elif num<rand:
        print("Guess is Low")
    else:
        print("U guessed it correct")
        print(f"Steps:{steps}")
        break;
