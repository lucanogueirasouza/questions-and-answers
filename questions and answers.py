import os
from time import sleep 

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
        clear_screen()
        return (
            "YOU GOT IT RIGHT!"
        )

    elif x != y: 
        wrong_answers += 1 
        clear_screen()
        return (
            "YOU WERE WRONG!"
        )
    
def clear_screen(): 
    os.system("Cls")

def sleep_screen(): 
    sleep(1)

question_1 = (print(
    "QUESTION 1) WHAT IS 2+2?\nA) 2\nB) 4\nC) 6"
    ))
CORRECT_ANSWER1 = "B"
person_answer1 = str(input(
    "TYPE YOUR ANSWER: "
)).upper().strip()
print (questions(person_answer1,CORRECT_ANSWER1))
sleep_screen()
clear_screen()

print (
    "-=-"*10
)
question_2 = (print(
    "QUESTION 2) WHAT IS 7/7?\nA) 2\nB) 8\nC) 1"
    ))
CORRECT_ANSWER2 = "C"
person_answer2 = str(input(
    "TYPE YOUR ANSWER: "
)).upper().strip()
print (questions(person_answer2,CORRECT_ANSWER2))
sleep_screen()
clear_screen()

print (
    "-=-"*10
)

question_3 = (print(
    "QUESTION 3) HOW MUCH IS 10*2?\nA) 30\nB) 20\nC) 50"
    ))
CORRECT_ANSWER3 = "B"
person_answer3 = str(input(
    "TYPE YOUR ANSWER: "
)).upper().strip()
print (questions(person_answer3,CORRECT_ANSWER3))
sleep_screen()
clear_screen()

print (
    f"FINAL CLASSIFICATION:\n\nSUCCESSES: {correct_answers}\nERRORS: {wrong_answers}"
)
