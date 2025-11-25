'''
GRADEBOOK ANALYSER
submitter by : NEHA
date : 25 nov.2025
description : A  python CLI tool to analyse student grades, import data manually or from CSV , compute statistics , assign drades , filter  results , and print formatted reports

'''





import csv


# calculate grade
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Manual Data Entry

def enter_data_manual():
    marks = {}

    while True:
        name = input("Enter student name (or 'stop' to finish): ")
        if name.lower() == "stop":
            break

        try:
            score = int(input("Enter marks (0-100): "))
        except ValueError:
            print("Invalid input! Enter numbers only.")
            continue

        marks[name] = score

    return marks



# CSV Import (Fixed Version)

def import_from_csv():
    filename = input("Enter CSV filename (example: student_data.csv): ")

    marks = {}

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header if present

            for row in reader:

                # Skip empty or invalid rows
                if len(row) < 2:
                    continue
                if row[0].strip() == "" or row[1].strip() == "":
                    continue

                try:
                    name = row[0].strip()
                    score = int(row[1].strip())
                    marks[name] = score
                except ValueError:
                    print(f"Skipping invalid marks for: {row}")
                    continue

        print("\nCSV Data Imported Successfully!\n")
        return marks

    except FileNotFoundError:
        print("\n❌ File not found! Please check the filename.\n")
        return {}



# Display Report

def display_report(marks):
    print("\n========== STUDENT REPORT ==========")

    for name, score in marks.items():
        grade = calculate_grade(score)
        print(f"{name}: Marks = {score} | Grade = {grade}")

    print("====================================\n")



# Main Menu

def main():

    print("========== GRADEBOOK ANALYZER ==========")
    print("1. Enter student data manually")
    print("2. Import student data from CSV")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        marks_dict = enter_data_manual()
        display_report(marks_dict)

    elif choice == "2":
        marks_dict = import_from_csv()
        display_report(marks_dict)

    elif choice == "3":
        print("Exiting Program...")
        exit()

    else:
        print("Invalid choice! Please choose 1, 2, or 3.")



# Run Program

if __name__ == "__main__":
    while True:
        main()
