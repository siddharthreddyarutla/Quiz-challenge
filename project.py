print("\nHey! there, welcome to the quiz game!")
print("\nHere you need to answer 10 questions according to that the score will be awarded and percentage as well")
print("\nNOTE: -1 for every incorrect answer")

playing = input("\nwanna play?(yes/no): ")

if playing.lower() != "yes":
    quit()
    
print("\nlets begin :)")
quiz_score=0
print("\n")
question  = input("who is the richest person in the world? ")
if question.lower() == "elon musk":
    print("correct!")
    quiz_score+=1
else:
    quiz_score-=1
    print("incorrect")
    
question  = input("who is the richest person in the Asia? ")
if question.lower() == "mukesh ambani":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect")
    quiz_score-=1

question = input("Entomology is the science that studies? ")
if question.lower() == "insects":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("Garampani sanctuary is located in which state? " )
if question.lower() == "assam":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("Hitler party which came into power in 1933 is known as? ")
if question.lower() == "nazi party":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("Golf player Vijay Singh belongs to which country? ")
if question.lower() == "fiji":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("First Afghan War took place in? ")
if question.lower() == "1839":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("First China War was fought between? ")
if question.lower() == "china and britain":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("Each year World Red Cross and Red Crescent Day is celebrated on? ")
if question.lower() == "may 8":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

question = input("Gravity setting chambers are used in industries to remove? ")
if question.lower() == "suspended particulate matter":
    print("correct!")
    quiz_score+=1
else:
    print("incorrect!")
    quiz_score-=1

print("\ncongratulations! You have scored : " +  str(quiz_score))

print("\nYou got " + str((quiz_score/10)*100 ) + " % precentage")
print("\n")
print("Answers are:\n1.elon musk\n2.mukesh ambani\n3.insects\n4.assam\n5.nazi party\n6.fiji\n7.1839\n8.china and britain\n9.may 8\n10.suspended particular matter")
