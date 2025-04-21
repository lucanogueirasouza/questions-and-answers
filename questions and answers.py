print (
    "MATH QUIZ V1.0\n"
)

print (
    "-=-"*10 , "\n"
)

correct_answers = 0
wrong_answers = 0 

def questions(x,y): 
    global correct_answers , wrong_answers
    if x == y:
        correct_answers += 1
        return (
            "YOU GOT IT RIGHT!!"
        )
    elif x != y: 
        wrong_answers += 1 
        return (
            "YOU WERE WRONG!"
        )
        
question_1 = (print(
    "QUESTION 1) WHAT IS 2+2?\nA) 2\nB) 4\nC) 6"
    ))
correct_answer1 = "B"
person_answer1 = str(input(
    "TYPE YOUR ANSWER: "
)).upper().strip()
print (questions(person_answer1,correct_answer1))

print (
    "-=-"*10
)

question_2 = (print(
    "QUESTION 2) WHAT IS 7/7?\nA) 2\nB) 8\nC) 1"
    ))
correct_answer2 = "C"
person_answer2 = str(input(
    "TYPE YOUR ANSWER: "
)).upper().strip()
print (questions(person_answer2,correct_answer2))

print (
    "-=-"*10
)

question_3 = (print(
    "QUESTION 3) HOW MUCH IS 10*2?\nA) 30\nB) 20\nC) 50"
    ))
correct_answer3 = "B"
person_answer3 = str(input(
    "TYPE YOUR ANSWER: "
)).upper().strip()
print (questions(person_answer3,correct_answer3))

print (
    f"IT'S OVER!\nSUCCESSES: {correct_answers}\nERRORS: {wrong_answers}"
)






