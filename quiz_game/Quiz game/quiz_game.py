print("Hello, welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
print("Let's play :)")

score = 0

answer = input ("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("What POST stand for? ")
if answer == "power on self test":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("Which country won the world cup in 2022? ")
if answer == "Argentina":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input ("Who is Manchester City's manager? ")
if answer == "pep guardiola":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.") 

