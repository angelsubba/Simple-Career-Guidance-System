print("=" * 45)
print("       SIMPLE CAREER GUIDANCE SYSTEM")
print("=" * 45)

print("\nWelcome! Let's explore your career options.")

name = input("\nEnter your name: ").strip()

print("\nHello,", name + "!")

print("\nChoose your favourite subject:")
print("1. Mathematics")
print("2. Computer Science")
print("3. Biology")
print("4. Business Studies")

subject = input("Enter your choice (1-4): ").strip()

print("\nChoose your area of interest:")
print("1. Artificial Intelligence")
print("2. Web Development")
print("3. Data Analysis")
print("4. Cybersecurity")

interest = input("Enter your choice (1-4): ").strip()

print("\n" + "=" * 45)
print("           YOUR CAREER GUIDANCE")
print("=" * 45)

if subject not in ["1", "2", "3", "4"]:
    print("Invalid subject choice. Please run the program again.")

elif interest not in ["1", "2", "3", "4"]:
    print("Invalid interest choice. Please run the program again.")

elif interest == "1":
    print("Suggested Career: AI/ML Engineer")
    print("Skills to learn: Python, Mathematics, and Machine Learning")

elif interest == "2":
    print("Suggested Career: Web Developer")
    print("Skills to learn: HTML, CSS, and JavaScript")

elif interest == "3":
    print("Suggested Career: Data Analyst")
    print("Skills to learn: Python, SQL, and Data Visualization")

elif interest == "4":
    print("Suggested Career: Cybersecurity Analyst")
    print("Skills to learn: Networking, Linux, and Security Basics")

print("\nNote: These are general suggestions, not a guaranteed career outcome.")
print("Explore different fields before making a career decision.")

print("\nThank you for using our system, " + name + "!")
print("=" * 45)