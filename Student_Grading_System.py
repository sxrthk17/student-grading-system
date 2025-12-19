# STUDENT GRADING SYSTEM!
students = {}


def add_student():
    print("--Add New Student--")

    roll = (input("Enter Roll Number: ")).strip()
    while not roll.isdigit():
        print("Invalid")
        roll = (input("Enter Roll Number: ")).strip()
    roll = int(roll)
    if roll in students:
        print("Roll number already exists. Try updating instead.")
        return

    name = input("Enter Student's name: ").strip().title()

    print("\nEnter marks out of 100")
    maths = input("Maths: ")
    while not maths.isdigit() or not (0 <= int(maths) <= 100):
        print("Invalid marks!")
        maths = input("Maths: ")
    oop = input("OOP: ")
    while not oop.isdigit() or not (0 <= int(oop) <= 100):
        print("Invalid marks")
        oop = input("OOP: ")
    dsa = input("DSA: ")
    while not dsa.isdigit() or not (0 <= int(dsa) <= 100):
        print("Invalid marks")
        dsa = input("DSA: ")

    maths, oop, dsa = int(maths), int(oop), int(dsa)
    total = maths + oop + dsa
    percentage = round(total/3, 2)
    grade = get_grade(percentage)

    students[roll] = {
        'name': name,
        'marks': {
            'maths': maths,
            'oop': oop,
            'dsa': dsa},
        'total': total,
        'percentage': percentage,
        'grade': grade
    }


def get_grade(percentage):
    if percentage >= 95:
        return "A++"
    elif 90 <= percentage < 95:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    else:
        return "F"


def delete_student():
    if not students:
        print("No students data to delete")
        return

    show_students()
    roll = input("Enter roll number to delete").strip()
    while not roll.isdigit():
        print("Please enter a number!")
        roll = input("Enter roll number to delete").strip()

    roll = int(roll)
    if roll in students:
        removed_student = students.pop(roll)
        print(f"Removed Student : {roll} - {removed_student['name']}")
    else:
        print("Roll number not found!")


def show_students():
    if not students:
        print("No students to display!")
        return

    for roll, data in students.items():
        print('-----------------------')
        print(f"Roll Number: {roll}")
        print(f"Name:{data['name']}")
        print("Marks:")
        print(f"Maths : {data['marks']['maths']}")
        print(f"OOP: {data['marks']['oop']}")
        print(f"DSA: {data['marks']['dsa']}")
        print(f"Total : {data['total']}")
        print(f"Percentage :{data['percentage']}")
        print(f"Grade: {data['grade']}")
        print('-----------------------')


def search_student():
    if not students:
        print("No students data available")
        return
    search = input("Search by Roll No. or Name?: ").lower()
    while search not in ['roll', 'name']:
        search = input("Search by Roll No. or Name?: ").lower()
    if search == 'roll':
        roll = input("Enter roll number to search: ")
        while not roll.isdigit():
            print("Roll number must be in digit!")
            roll = input("Enter roll number to search: ")
        roll = int(roll)
        if roll in students:
            data = students[roll]  # imp
            print("-----------------------")
            print("STUDENT FOUND!")
            print('-----------------------')
            print(f"Roll Number: {roll}")
            print(f"Name:{data['name']}")
            print("Marks:")
            print(f"Maths : {data['marks']['maths']}")
            print(f"OOP: {data['marks']['oop']}")
            print(f"DSA: {data['marks']['dsa']}")
            print(f"Total : {data['total']}")
            print(f"Percentage :{data['percentage']}")
            print(f"Grade: {data['grade']}")
            print('-----------------------')
        else:
            print("Roll number not found")
    elif search == "name":
        name = input("Enter name to search: ").strip().lower()
        found = False
        for roll, data in students.items():
            if data['name'].lower() == name:
                found = True
                print("-----------------------")
                print("STUDENT FOUND!")
                print('-----------------------')
                print(f"Roll Number: {roll}")
                print(f"Name:{data['name']}")
                print("Marks:")
                print(f"Maths : {data['marks']['maths']}")
                print(f"OOP: {data['marks']['oop']}")
                print(f"DSA: {data['marks']['dsa']}")
                print(f"Total : {data['total']}")
                print(f"Percentage :{data['percentage']}")
                print(f"Grade: {data['grade']}")
                print('-----------------------')
        if not found:
            print("No students found with that name!")


def update_student():
    if not students:
        print("No student data to update!")
        return
    roll = input("Which Roll no. to update?: ")
    while not roll.isdigit():
        print("Roll number must be digit")
        roll = input("Which Roll no. to update?: ")
    roll = int(roll)

    if roll not in students:
        print("Roll number not found!")
        return

    student = students[roll]
    print("What do you want to update?")
    print("1.Name\n2.Marks\n3.Both Name and Marks")

    choice = input("Enter choice (1/2/3): ").strip()
    while choice not in ['1', '2', '3']:
        choice = input("Enter choice (1/2/3): ").strip()

    if choice == '1' or choice == '3':
        new_name = input("Enter new name: ").strip()
        while not new_name.replace(" ", "").isalpha():
            print("Name should be in characters only!")
            new_name = input("Enter new name: ").strip()
        student['name'] = new_name

    if choice == '2' or choice == '3':
        print("Enter new marks:")

        maths = input("Maths: ").strip()
        while not maths.isdigit() or not (0 <= int(maths) <= 100):
            print("Marks should be between 0 and 100!")
            maths = input("Maths: ").strip()

        oop = input("OOP: ").strip()
        while not oop.isdigit() or not (0 <= int(oop) <= 100):
            print("Marks should be between 0 and 100!")
            oop = input("OOP: ").strip()

        dsa = input("DSA: ").strip()
        while not dsa.isdigit() or not (0 <= int(dsa) <= 100):
            print("Marks should be between 0 and 100!")
            dsa = input("DSA: ").strip()

        student['marks']['maths'] = int(maths)
        student['marks']['oop'] = int(oop)
        student['marks']['dsa'] = int(dsa)

        total = student['marks']['maths'] + \
            student['marks']['oop'] + student['marks']['dsa']
        percentage = round(total/3, 2)
        grade = get_grade(percentage)

        student['total'] = total
        student['percentage'] = percentage
        student['grade'] = grade

        print("\nStudent updated successfully!")
        print("-----------------------")
        print(f"Roll Number: {roll}")
        print(f"Name: {student['name']}")
        print("Marks:")
        print(f"Maths: {student['marks']['maths']}")
        print(f"OOP: {student['marks']['oop']}")
        print(f"DSA: {student['marks']['dsa']}")
        print(f"Total: {student['total']}")
        print(f"Percentage: {student['percentage']}")
        print(f"Grade: {student['grade']}")
        print("-----------------------")


def class_topper():
    if not students:
        print("No students data available!")
        return
    max_total = -1
    topper = None
    toppers_roll = 0

    for roll, student in students.items():
        if student['total'] > max_total:
            max_total = student['total']
            topper = student
            toppers_roll = roll
    print("-----------------------")
    print("Overall Topper:")
    print(f"{toppers_roll}")
    print(f"Name: {topper['name']}")
    print(f"Total Marks: {topper['total']}")
    print(f"Percentage: {topper['percentage']:.2f}%")
    print(f"Grade: {topper['grade']}")
    print("-----------------------")


def subject_topper(subject_name):
    if not students:
        print("No students data available!")
        return

    if subject_name == "maths":
        max_math_marks = -1
        maths_topper = None
        maths_topper_roll = 0

        for roll, student in students.items():
            if student['marks']['maths'] > max_math_marks:
                max_math_marks = student['marks']['maths']
                maths_topper = student
                maths_topper_roll = roll
        print("-----------------------")
        print("Maths Topper")
        print(f"{maths_topper_roll}")
        print(f"Name: {maths_topper['name']}")
        print(f"Math Marks: {max_math_marks}")
        print(f"Total = {maths_topper['total']}")
        print(f"Grade = {maths_topper['grade']}")
        print("-----------------------")

    elif subject_name == "oop":
        max_oop_marks = -1
        oop_topper = None
        oop_topper_roll = 0

        for roll, student in students.items():
            if student['marks']['oop'] > max_oop_marks:
                max_oop_marks = student['marks']['oop']
                oop_topper = student
                oop_topper_roll = roll
        print("-----------------------")
        print("OOP TOPPER")
        print(f"{oop_topper_roll}")
        print(f"Name: {oop_topper['name']}")
        print(f"OOP Marks: {max_oop_marks}")
        print(f"Total = {oop_topper['total']}")
        # THhis thing can be made a function !
        print(f"Grade = {oop_topper['grade']}")
        print("-----------------------")

    elif subject_name == "dsa":
        max_dsa_marks = -1
        dsa_topper = None
        dsa_topper_roll = 0

        for roll, student in students.items():
            if student['marks']['dsa'] > max_dsa_marks:
                max_dsa_marks = student['marks']['dsa']
                dsa_topper = student
                dsa_topper_roll = roll
        print("-----------------------")
        print(" TOPPER")
        print(f"{dsa_topper_roll}")
        print(f"Name: {dsa_topper['name']}")
        print(f"DSA Marks: {max_dsa_marks}")
        print(f"Total = {dsa_topper['total']}")
        print(f"Grade = {dsa_topper['grade']}")
        print("-----------------------")
    else:
        print("Enter a valid subject!")


def main():
    print("Student Grading System")
    is_running = True
    while is_running:
        print("|1.Add Student")
        print("|2.Delete student")
        print("|3.Show Student")
        print("|4.Search student")
        print("|5.Update student")
        print("|6.Class Result")
        print("|7.Subject Topper")
        print("|8.Exit")

        choice = input("Whats do you want to do? ")

        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            show_students()
        elif choice == '4':
            search_student()
        elif choice == '5':
            update_student()
        elif choice == "6":
            class_topper()
        elif choice == "7":
            subject_name = input("Enter the subject: (Maths/OOP/DSA)").lower()
            while subject_name not in ['maths', 'oop', 'dsa']:
                print("Enter a valid subject: ")
                subject_name = input(
                    "Enter the subject: (Maths/OOP/DSA)").lower()
            subject_topper(subject_name)
        elif choice == '8':
            break
        else:
            print("Please enter a valid choice! ")


if __name__ == "__main__":
    main()
