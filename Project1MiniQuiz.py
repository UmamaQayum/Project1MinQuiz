print("Welcome to my computer Quiz!")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()

print("Great! Let's play!")
score = 0

Question1 = input("What does CPU stand for? ")
if Question1.strip().lower() == "central processing unit":
    print("Correct!")
    score += 1
else:   
    print("Incorrect")

Question2 = input("What does GPU stand for? ")
if Question2.strip().lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
Question3 = input("What does RAM stand for? ")
if Question3.strip().lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%.")
