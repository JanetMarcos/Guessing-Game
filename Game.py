print("Hello World") 
GuessName = int(input("Enter your number: "))
count = 1
userNum = 0
while GuessName != userNum:
    userNum = int(input("Enter your guessed number: "))

    count = count +1
    if userNum > GuessName:
        print("Guess lower")
    else:
        print ("Guess higher")
print ("YOU HAVE WON!")
    
