'''
This is a simple quiz game that tests the user's knowledge of Africa.
The user will be asked a series of questions about Africa and will need to answer correctly to proceed.
The user's goal is to answer three (3) questions correctly in a row.
A preamble function will give the user some basic information about Africa and the quiz.
Best of luck!
'''

# import the Json module
import json

# load the data 
with open('africa_facts_dictionary.json', 'r') as file:
    africa_facts = json.load(file)
    # print(africa_facts)

# Define a preamble function to give the user some basic guidelines
def preamble():
    '''
    This function give the user some basic information about Africa and the quiz. 
    It informs the user how scoring will be done in the quiz.
    '''
    preamble_text = ["Welcome to the African Facts Quiz!", 
                     "You will be asked a series of questions about Africa.",
                     "Your goal is to answer three (3) questions correctly in a row."]
    for line in preamble_text:
        print(line)
    print(" ")

    print("Africa is the second largest continent in the world. It has 54 countries.")
    countries = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
    "Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
    "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau",
    "Ivory Coast", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar",
    "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique",
    "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe",
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa",
    "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia",
    "Zimbabwe"
    ]
    print("The countries in Africa include: " + "\n ".join(countries))
    print(" ")

    print("Now that you have some basic knowledge, Let's get started!")
    print(" ")

    
# Define a helper function to get a random fact and its answer from the list
def ask_question():
    import random
    fact = random.choice(africa_facts)
    question = fact["question"]
    answer = fact["answer"]
    return question, answer

# Define a helper function to ask the user to input their answer
def get_user_answer(question):
    user_answer = input(question + " ")
    # if the user input is empty, ask the user to input an answer
    while user_answer == "":
        print("Please input an answer.")
        user_answer = input(question + " ")
    return user_answer

# Define a helper function to check if the user's answer is correct
def assess_user_answer(user_answer, answers):
    return user_answer.lower() in [answer.lower() for answer in answers]

# Define the main function to run the quiz
def main():
    preamble()
    score = 0   # Initialize a score variable for the user

    while score < 3:  # Test user's African knowledge with three consecutive right answers
        question, answers = ask_question()
        user_answer = get_user_answer(question)

        # check user's answer
        if assess_user_answer(user_answer, answers):
            print("Correct! The right answer is: " + ", ".join(answers))
            score += 1
        else:
            print("Incorrect! The right answer is: " + ", ".join(answers))
            score = 0   # Reset the score to 0 if the user gets a question wrong
            print("You need to start over.")

        print("Your score is: " + str(score))
        print(" ")

    # print a congratulatory message
    print("Congratulations! You have successfully answered 3 questions correctly in a row.")
if __name__ == "__main__":
    main()