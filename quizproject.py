def new_game():
    guesses = []
    correct_guess = 0
    question_num = 1
    for i in questions:
        print("--------------------------")
        print(i)
        for j in options[question_num-1]:
            print(j)
        guess = input("Enter (A ,B ,C ,D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guess+=check_ans(questions.get(i),guess)
        question_num+=1
    display_score(correct_guess, guesses)
#----------------------

def check_ans(answer,guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
#----------------------

def display_score(correct_guess, guesses):
    print("------------------------")
    print("Result")
    print("------------------------")
    print("Answer: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Gusses: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()
    score = int((correct_guess/len(questions))*100)
    print("Your score is " , str(score) , "%" )
#----------------------



#28,HOCKEY,PEACOCK,NAMO


questions = {
        "how many state in india?":"A",
        "what is national game of india?":"C",
        "what is nation bird if india?":"D",
        "who is present prime minister of india?":"B",
    }

options = [["A. 28","B. 30","C. 19","D. 32"],
           ["A. Cricket","B. Footbal","C. Hockey","D. Basketball"],
           ["A. Eagel","B. Ostrich","C. Pijeon","D. Peacock"],
           ["A. Rahul gandhi","B. Narendra Modi","C. Arvind kejriwal","D. Sandesh gaikwad"],
           ]

new_game()
