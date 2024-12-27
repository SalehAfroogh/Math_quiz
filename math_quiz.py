
import random
import time
def question_generator():
    a = random.randint(1,9)
    b = random.randint(1,9)
    
    operator_list= ["-", "+", "*"]
    selected_operator = random.choice(operator_list)
    
    print(f"{a} {selected_operator} {b}= ?")
    
    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b 

question_number_limit = 5
question_number = 0
score = 0
time_lim = 5

while question_number < question_number_limit:
    # generate random questions
    result = str(question_generator())
    print(result)
    start_time = time.time()
    
    # get user answer
    
    user_answer = input("Enter your answer: ")
    end_time = time.time()
    
    time_dif = end_time - start_time
    # check answer
    if time_dif < time_lim:
        if result == user_answer:
            score += 1
            print (f"Perfect! Your score is {score}") 
        else:
            print(f"Sorry, it is wrong. Your score is {score}")
    else:
        print(f"You are too late! Your score is {score}")    
    question_number += 1
    
print(f"Final score is {score} out of {question_number_limit} question")
    