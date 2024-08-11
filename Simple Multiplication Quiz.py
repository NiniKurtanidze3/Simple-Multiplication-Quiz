from random import randint

print("Welcome to the Simple Multiplication Quiz! \nYou will be given 5 multiplication problems to solve")

n = 0
problem_num = 1
score = 0

while n < 5:
    a, b = randint(1, 10), randint(1, 10)
    correct_answer = a * b
    print(f"problem {problem_num}: What is {a} x {b}?")
    user_input = input("Your answer: ")

    if user_input.isdigit() and int(user_input) == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {correct_answer}")

    n += 1
    problem_num += 1

if score <= 3:
    print(f"You scored {score} out of {problem_num - 1}. You need to practice more!")
else:
    print(f"You scored {score} out of {problem_num - 1}. Well done!")

