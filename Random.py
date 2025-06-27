import random
import math
import time
score = 0
name = input("Enter your name: ")
start_time = time.time()  
print("Hii!", name, "Welcome to the Square and Square Root Game!")

while True:
    question_type = random.choice(['square', 'square_root'])

    if question_type == 'square':
        num = random.randint(1, 100)
        print(f"\nWhat is the square of {num}?")
        question_start = time.time()  

        try:
            ans = int(input("Enter your answer: "))
            time_taken = round(time.time() - question_start, 2)  # Time in seconds

            correct = num*num
            if ans == correct:
                print(" Correct!")
                score += 10
                print(f"You took {time_taken} seconds to answer.")
                print("Your score is:", score)

            else:
                
                print(f" Wrong! The correct answer was {correct}.")
                score -= 5
                print(f"You took {time_taken} seconds to answer.")
                print("Your score is:", score)

        except ValueError:
            print(" Please enter a valid number.")

    else:  
        root = random.randint(1, 100)
        num = root * root
        print(f"\nWhat is the square root of {num}?")
        question_start = time.time()  

        try:
            ans = int(input("Enter your answer: "))
            time_taken = round(time.time() - question_start, 2)  # Time in seconds

            correct = int(math.sqrt(num))
            if ans == correct:
                print(" Correct!")
                score += 10
                print(f"You took {time_taken} seconds to answer.")
                print("Your score is:", score)

            else:
                print(f" Wrong! The correct answer was {correct}.")
                score -= 5
                print("Your score is:", score)
                print(f"You took {time_taken} seconds to answer.")
        except ValueError:
            print(" Please enter a valid number.")

        if score >= 50:
           print(" Congratulations! You are a winner!")
           print("Final Score:", score)
           print("Total time spent:", time_taken)
           break

    choice = input("\nDo you want to continue the  Quiz? (yes/no): ").strip().lower()
    if choice != 'yes':
          end_time = time.time()
          total_time = round(end_time - start_time, 2)
          print(f"\nYOU ARE LOOSER!.. Final Score: {score}")
          print(f" Total time spent in quiz: {total_time} seconds")
          break

