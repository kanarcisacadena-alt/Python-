import csv
import os

#-------------------------------------------------------------------------------------------------

def register_student():
    try:
        with open("student/students.csv", "a", newline="") as file:
            add = csv.DictWriter(file, fieldnames=["id","name", "age","career","grade"])

            if os.path.getsize("student/students.csv") == 0:
                add.writeheader()

            print ("===== REGISTER STUDENT =====")   
            name = input("Enter student name: ").title()
            age = input("Enter student age: ")  
            career = input("Enter student career: ").title()
            grade = input("Enter student grade: ")

            if correct_student_data(name, age, career, grade):

                id = sum(1 for row in csv.DictReader(open("student/students.csv")))+1

                add.writerow({"id": id, "name": name, "age": age, "career": career, "grade": grade})

                print(f"Student {name} registered successfully!")

            else:
                print("Student registration failed due to invalid data.")
      
    except FileNotFoundError as e:
        with open("student/students.csv", "r") as file:
            pass

######## Esta es para validar los datos del estudiante antes de registrarlo

def correct_student_data(name, age, career, grade):
    if not name.isalpha():
        print("Invalid name. Please enter a valid name.")
        return False
    if not age.isdigit() or int(age) <= 0:
        print("Invalid age. Please enter a positive integer.")
        return False
    if not career.isalpha():
        print("Invalid career. Please enter a valid career.")
        return False
    if not grade.replace('.', '', 1).isdigit() or float(grade) < 0 or float(grade) > 100:
        print("Invalid grade. Please enter a number between 0 and 100.")
        return False
    return True

#----------------------------------------------------------------------------------------------------

def show_students():
    with open("student/students.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"ID: {row['id']}, Name: {row['name']}, Age: {row['age']}, Career: {row['career']}, Grade: {row['grade']}")


#----------------------------------------------------------------------------------------------------

def search_student():
    search_name = input("Enter the name of the student to search: ").title().strip()
    with open("student/students.csv", "r") as file:
        finder = csv.DictReader(file)
        finded = False

        for row in finder:
            if row["name"] == search_name:
                print(f"ID: {row['id']}, Name: {row['name']}, Age: {row['age']}, Career: {row['career']}, Grade: {row['grade']}")
                finded = True

        if not finded:
            print(f"Student with name {search_name} not found.")
#----------------------------------------------------------------------------------------------------

def update_student_grade():
    update_name = input("Enter the name of the student to update grade: ").title().strip()
    with open("student/students.csv", "r") as file:
        reader = csv.DictReader(file)

        if not any(row["name"] == update_name for row in reader):
            print(f"Student with name {update_name} not found.")
            return

        else:
            new_grade = input("Enter the new grade: ")

            if not new_grade.replace('.', '', 1).isdigit() or float(new_grade) < 0 or float(new_grade) > 100:
                print("Invalid grade. Please enter a number between 0 and 100.")
                return
            else:
                with open("student/students.csv", "r", newline="") as file:
                    rows = list(csv.DictReader(file))

                for row in rows:
                    if row["name"] == update_name:
                        row["grade"] = new_grade

                with open("student/students.csv", "w", newline="") as file:
                    writer = csv.DictWriter(
                        file,
                        fieldnames=["id", "name", "age", "career", "grade"]
                    )

                    writer.writeheader()
                    writer.writerows(rows)

#---------------------------------------------------------------------------------------------------

def delete_student():
    del_name = input("Enter the name of the student to delete: ").title().strip()

    with open("student/students.csv", "r") as file:
        rows = list(csv.DictReader(file))

    if not any(r["name"] == del_name for r in rows):
        print(f"Student with name {del_name} not found.")
        return

    else:
        with open("student/students.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["id", "name", "age", "career", "grade"]
            )

            for c in rows:
                if c["name"] == del_name:
                    delete_id = c["id"]
                    
            writer.writeheader()
            for r in rows:
                if r["name"] != del_name:
                    r["id"] = str(int(r["id"]) - 1) if r["id"] > delete_id else r["id"]  # Adjust ID for remaining students
                    writer.writerow(r)

#---------------------------------------------------------------------------------------------------

def show_statistics():

    """Total students: 12

    Average grade: 42.5

    Highest grade: 49
    Student: Ana

    Lowest grade: 28
    Student: Carlos

    Passing students: 10
    Failing students: 2
    """

    with open("student/students.csv", "r") as file:
        reader = csv.DictReader(file)
        students = list(reader)

        print(f"Total students: {len(students)}")
        print(f"Average grade: {sum(float(s['grade']) for s in students) / len(students):.2f}")

        for s in students:
            if float(s['grade']) == max(float(r['grade']) for r in students):
                print(f"Highest grade: {s['grade']}")
                print(f"Student: {s['name']}")

            if float(s['grade']) == min(float(r['grade']) for r in students):
                print(f"Lowest grade: {s['grade']}")
                print(f"Student: {s['name']}")

        for student in students:
            if float(student['grade']) >= 60:
                passing_students = sum(1 for s in students if float(s['grade']) >= 60)

            if float(student['grade']) < 60:
                failing_students = sum(1 for s in students if float(s['grade']) < 60)

        print(f"Passing students: {passing_students}")
        print(f"Failing students: {failing_students}")

#---------------------------------------------------------------------------------------------------

def main():

    while True:
        print("""
        ===== STUDENT MANAGER =====

        1. Register student
        2. Show all students
        3. Search student
        4. Update student grade
        5. Delete student
        6. Show statistics
        7. Exit

        Select an option:
        """)


        opc = input("Enter your choice (1-7): ")


        match opc:
            case "1":
                register_student()
            case "2":
                show_students()
            case "3":
                search_student()
            case "4":
                update_student_grade()
            case "5":
               delete_student()
            case "6":
                show_statistics()
                
            case "7":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option. Please try again.")

#---------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()