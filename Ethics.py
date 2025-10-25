# Ethics & Responsible Use Reflection
# Author: [Your Name]
# Version: 1.0

def ask_scale(question):
    """Ask a Likert-scale question (1–5) and validate input."""
    print(f"\n{question}")
    print("1 – Strongly disagree")
    print("2 – Disagree")
    print("3 – Neutral")
    print("4 – Agree")
    print("5 – Strongly agree")
    while True:
        try:
            value = int(input("Your answer (1–5): "))
            if 1 <= value <= 5:
                return value
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

def ask_open(question):
    """Ask an open-ended question (text response)."""
    print(f"\n{question}")
    input("Your response: ")
    # Open responses are not scored, only reflective.

def give_feedback(total):
    """Return qualitative feedback based on score range."""
    print("\n" + "-"*50)
    print(f"Total Score: {total}/40")
    print("-"*50)
    if total >= 35:
        print("🌟 Excellent reflection! You are aware of ethical and social implications and considered them in your project.")
    elif total >= 25:
        print("👍 Good reflection. Consider exploring deeper issues like bias, data handling, or social impact.")
    elif total >= 15:
        print("🟡 Some awareness shown. Review your understanding of privacy, fairness, and programmer responsibility.")
    else:
        print("⚠️ Review your project carefully. Think about potential risks, bias, and social impact in your code.")
    print("-"*50)

def ethics_reflection():
    print("="*60)
    print("SURVEY: Ethics & Responsible Use Reflection")
    print("="*60)
    print("Reflect on your final project and answer honestly.")
    print("There are no right or wrong answers — just your reflection.\n")

    score = 0

    # Section 1 – Social & Ethical Impact
    print("\nSECTION 1: Social & Ethical Impact")
    score += ask_scale("My project has a positive impact on users or society.")
    score += ask_scale("I considered potential risks or misuse of my project.")
    ask_open("Briefly describe one way your project could impact users positively and one potential risk.")

    # Section 2 – Privacy & Data Use
    print("\nSECTION 2: Privacy & Data Use")
    score += ask_scale("I handled user data responsibly in my project.")
    score += ask_scale("I implemented measures to protect privacy and data security.")
    ask_open("What would you change to improve privacy or data security in your project?")

    # Section 3 – Bias & Fairness
    print("\nSECTION 3: Bias & Fairness")
    score += ask_scale("My project avoids unfair advantages or disadvantages to certain users.")
    score += ask_scale("I reviewed my project for biases in recommendations, scoring, or output.")
    ask_open("Can you identify a potential bias in your project? How would you address it?")

    # Section 4 – Programmer Responsibility
    print("\nSECTION 4: Programmer Responsibility")
    score += ask_scale("I considered ethical implications when making programming decisions.")
    score += ask_scale("If my project had a real-world impact on many users, I would know how to improve it responsibly.")
    ask_open("Describe one programming decision you made with ethics in mind.")

    give_feedback(score)

# Run survey
if __name__ == "__main__":
    ethics_reflection()
