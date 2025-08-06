import json

# ---------------- Diary App ----------------

notes = {}   # Temporary dictionary for a single note
diary = []   # List to store all notes

def add_notes():
    # Loop until user enters a valid title (not empty or just spaces)
    while True:
        title = input("Add a title to the note: ")
        if (title.strip() == ""):
            print("Title cannot be empty or just a space!")
        else:
            break
    # Loop until user enters a valid note (not empty or just spaces)
    while True:
        note = input("Enter the note: ")
        if (note.strip() == ""):
            print("Note cannot be empty or just a space!")
        else:
            new_note = {title: note}  # Create a dictionary for the note
            break

    # Try to read existing notes from Diary.json, or start with empty list if file doesn't exist/corrupted
    try:
        with open("Diary.json", "r") as file:
            diary = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        diary = []

    diary.append(new_note)  # Add the new note to the diary list

    # Save the updated diary list back to Diary.json
    with open("Diary.json", "w") as file:
        json.dump(diary, file, indent=4)


def view_all_notes():
    # Try to read and display all notes from Diary.json
    try:
        with open("Diary.json", "r") as file:
            data = json.load(file)
        for i in data:
            print(i)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found or is corrupted")


def search_by_title():
    # Loop until user enters a valid title to search
    while True:
        title_select = input("Enter the title to search in the diary database: ")
        if (title_select.strip() == ""):
            print("You cannot leave the input blank or enter just space!")
        else:
            break
    
    # Try to find and display the note with the given title
    try:
        with open("Diary.json", "r") as file:
            notes = json.load(file)
        found = False
        for i in notes:
            if (title_select in i):
                print("=" * 80)
                print(f"{title_select}: {i[title_select]}")
                found = True
                break
        if not found:
            print("Title not found")
            print("Causes:")
            print("1. No note created with the above title\n 2. Spelling mistake while entering the title")
            print("Please try again....")
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found or is corrupted!")

# ---------------- UI & Main Loop ----------------

class WrongInputError(Exception):
    pass

while True:
    print("~" * 80)
    print("Hello User!!")
    print("Welcome to Diary app - By Pranav")
    print("~"* 80)

    functions = ["Add note", "View all notes", "Search by title"]

    # Display available functions with numbering using enumerate
    print("App functions:")
    for idx, func in enumerate(functions, start=1):
        print(f"{idx}. {func}")
    print("=" * 80)
    # Loop until user enters a valid function number
    while True:
        try:
            choice = int(input("Enter the function number to perform the function (1-3): "))
            if(choice > 3 or choice <= 0):
                print("Please enter a valid function number")
            else:
                break
        except ValueError as e:
            print("Error:", e)          

    # Call the selected function
    if (choice == 1):
        add_notes()
    elif (choice == 2):
        view_all_notes()
    elif (choice == 3):
        search_by_title()

    # Ask user if they want to perform another function
    again_choices = ["yes", "y", "ya", "no", "n", "nah"]
    yes_choice = ["yes", "y", "ya"]
    no_choice = ["no", "n", "nah"]
    try:
        print('=' * 80)
        again = input("Do you want to perform any other functions (Yes / No): ").lower()
        print('=' * 80)
        if (again not in again_choices):
            raise WrongInputError("Please enter yes or no")
        elif (again in no_choice):
            print("~" * 80)
            print("Thanks for using our app.....")
            print("~" * 80)
            break
        elif (again in yes_choice):
            continue
    except WrongInputError as e:
        print("Error:", e)