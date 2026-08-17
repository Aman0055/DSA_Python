print("Welcome to the Quiz game !!")

playing = input("Do you want to play the game ? (yes/no) : ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game !!")
score = 0

answer = input("What does cpu stand for ? :")
if answer.lower() == "central processing unit":
    print("Correct answer !!")
    score += 1
else:
    print("Incorrect answer !!")

answer = input("what does gpu stand for ?")
if answer.lower() == "graphics processing unit":
    print("Correct answer !!")
    score += 1
else:
    print("Incorrect answer !!")

answer = input("what does ram stand for ?")
if answer.lower() == "random access memory":
    print("Correct answer !!")
    score += 1
else:
    print("Incorrect answer !!")

answer = input("what does ps stand for ?")
if answer.lower() == "play station":
    print("Correct answer !!")
    score += 1
else:
    print("Incorrect answer !!")

print("You got " + str(score) + " questions correct !!")
