print("Welcome to Nature quiz game!!")
play = input("Do you want to play the quiz?? ")
if play.lower() != "yes":
    quit()
print("Okay! let's play the quiz")
score = 0
ans = input("Which is the fastest moving land snake in the world? ")
if ans.lower() == "black mamba":
    print("correct!!")
    score+=1
else:
    print("incorrect the answer is black mamba")

ans = input("Delphinus delphis is the scientific name for which creature? ")
if ans.lower() == "dolphin":
    print("correct!!")
    score+=1
else:
    print("incorrect the answer is dolphin")

ans = input("What type of creature is a Dog Face? ")
if ans.lower() == "butterfly":
    print("correct!!")
    score+=1
else:
    print("incorrect the answer is Butterfly")
ans = input("How many toes does a cat have on each front paw? ")
if ans.lower() == "five":
    print("correct!!")
    score+=1
else:
    print("incorrect the answer is five")
ans = input("What is a female alligator called? ")
if ans.lower() == "cow":
    print("correct!!")
    score+=1
else:
    print("incorrect the answer is cow")
print("you got "+ str(score) +" questions coreect ")