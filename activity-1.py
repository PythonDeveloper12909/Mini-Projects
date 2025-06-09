print("welcome to the ai chatbot!")
name=input("what is your name? ")
print("hello " + name + ", how is your mood today good or bad?")
mood=input().lower()
if mood=="good":
    print("I am glad to hear that " + name + "!")
elif mood=="bad":
    print("i am sorry to hear that" + name + ".i hope everything will be fine soon!")
else:
    print("i am not sure exactly what your are saying "+ name + ",but i hope everything will be fine")
print("goodbye " +name+ " have a great day ahead!")