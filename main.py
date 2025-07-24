import time

def get_high_score():
    try: 
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
            return 0 #if no file found, return 0
    
def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))

def run_quiz():
    start_time = time.time()

    def choose_difficulty():
        print("Choose a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter the number of your choice: ").strip()
        while choice not in ["1", "2", "3"]:
            print("invalid choice. Please choose 1, 2, or 3.")
            choice = input("Enter the number of your choice:").strip()
        
        if choice == "1":
            return easy_questions
        elif choice == "2":
            return medium_questions
        elif choice == "3":
            return hard_questions
    
    easy_questions = [
        {
            "question": "What is the capital of Indonesia?",
            "options": ["A. Jakarta", "B. Makassar", "C. Bandung", "D. Surabaya"],
            "answer": "A",
            "levels": "easy"
        },
        {
            "question": "Which language is used to build websites?",
            "options": ["A. Python", "B. HTML", "C. Java", "D. C++"],
            "answer": "B",
            "levels": "easy"
        },
        {
            "question": "What does RAM stand for?",
            "options": ["A. Readily Accessible Memory", "B. Random Access Memory", "C. Rapid Application Machine", "D. Read And Modify"],
            "answer": "B",
            "levels": "easy"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "C",
            "levels": "easy"
        },
        {
            "question": "Where is Petronas foundations located?",
            "options": ["A. Indonesia", "B. Malaysia", "C. Singapore", "D. Thailand"],
            "answer": "B",
            "levels": "easy"
        }]
    medium_questions = [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. O2", "B. H2O", "C. CO2", "D. NaCl"],
            "answer": "B",
            "levels": "medium"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
            "answer": "C",
            "levels": "medium"
        },
        {
            "question": "Who is the writer of breaking bad?",
            "options": ["A. Vince Gilligan", "B. David Chase", "C. Aaron Sorkin", "D. J.J. Abrams"],
            "answer": "A",
            "levels": "medium"
        },
        {
            "question": "Who is the 2024 F1 championship?",
            "options": ["A. Max verstappen", "B. Lewis Hamilton", "C. Sebastian Vettel", "D. Fernando Alonso"],
            "answer": "A",
            "levels": "medium"
        },
        {
            "question": "Who is the championship motogp 2024?",
            "options": ["A. Marc Marquez", "B. Alex Rins", "C. Francesco Bagnaia", "D. Jorge Martin"],
            "answer": "D",
            "levels": "medium"
        }]
    hard_questions = [ 
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A",
            "levels": "hard"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
            "answer": "C",
            "levels": "hard"
        },
        {
            "question": "How does pablo escobar die?",
            "options": ["A. In a car accident", "B. In a shootout with police", "C. Poisoning", "D. Natural causes"],   
            "answer": "B",
            "levels": "hard"
        },
        {
            "question": "Who is the best Counter-Strike2 player in 2024?",
            "options": ["A. donk", "B. ZywOo", "C. dev1ce", "D. Niko"],
            "answer": "A",
            "levels": "hard"
        },
        {
            "question": "who is the creator of roblox?",
            "options": ["A. David Baszucki", "B. Markus Persson", "C. Gabe Newell", "D. John Carmack"],
            "answer": "A",
            "levels": "hard"
        }]

    questions = choose_difficulty()
    
    score = 0

    print("🧠 Welcome to the Quiz Game!")
    print("---------------------------")

    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")
        for option in q["options"]:
            print(option)

        # TODO: Get the user's answer
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid option. please choose A,B,C, or D.")
            answer = input("Your answer (A/B/C/D): ").strip().upper()
      
        # TODO: Check if the answer is correct
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

          # Validate the answer input        
    print("\n🎉 Quiz Finished!")
    print("---------------------------")
    high_score = get_high_score()
    print(f"\nYour Score: {score}/ {len(questions)}")

    # Save new high score if beaten
    if score > high_score:
        save_high_score(score)
        print("🎉 New high score!")
    else:
        print(f"High Score: {high_score}")

    end_time = time.time() #end timer
    elapsed_time = round(end_time - start_time, 1) #calculate elapsed time
    print(f"You finished the quiz in {elapsed_time} seconds.")

def main_menu():
    while True:
        print("\n🎮 Quiz Game Menu")
        print("1. Start Game")
        print("2. View High Score")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            run_quiz()
        elif choice == "2":
            print(f"Current High Score: {get_high_score()}")
        elif choice == "3":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

#run_quiz()