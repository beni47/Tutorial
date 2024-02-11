#Ask for users answer on the question
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

#just a list with the answers
answers = ("42","forty two","forty-two")

#check if answer is correct
if answer in answers:
    print("Yes")
else:
    print("No")


#print outcome
