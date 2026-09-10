print("Welcome to the Launch Console")
print("My name is Anish, what is your's")
Your_name = input("What is your name ")
print(f"Hi {Your_name} I am happy your are here")
running = True
while running:
    print("1) About Me ")
    print("2) My Goals ")
    print("3) My Hobbies ")
    print("4) Exit")
    choice = input("Pick what you want to know about me 1-4!")
    if choice == "1":
        print("I am Anish Gunturi, I am a junoir going to vista ridge high school. I am taking the Code2Collage program.")
    elif choice == "2":
        print("My goals are to get into a good collage in state and to land an intership with the code to collage program.")
    elif choice == "3":
        print("My hobbies are to draw read books and hang out with my friends.")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick a number from 1-4")