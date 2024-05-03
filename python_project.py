class Hostel:
    # Initialize the Hostel object with name and capacity
    def __init__(self, name, capacity):
        self.name = name  # Name of the hostel
        self.capacity = capacity  # Maximum number of students it can accommodate
        self.students = []  # List to store students currently in the hostel

    # Method to add a student to the hostel
    def add_student(self, student):
        # Check if there is space in the hostel
        if len(self.students) < self.capacity:
            self.students.append(student)  # Add the student to the hostel
            print(f"{student.name} has been added to {self.name}.")  # Print a message
        else:
            print(f"{self.name} is full. Cannot add {student.name}.")  # Print a message if hostel is full

    # Method to remove a student from the hostel
    def remove_student(self, student_name):
        # Check if the student is in the hostel
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)  # Remove the student from the hostel
                print(f"{student_name} has been removed from {self.name}.")  # Print a message
                return
        print(f"{student_name} is not in {self.name}.")  # Print a message if student is not in hostel

    # Method to list all students in the hostel
    def list_students(self):
        print(f"Students in {self.name}:")  # Print the name of the hostel
        for student in self.students:  # Iterate over each student in the hostel
            print(student.name)  # Print the name of the student

    # Method to search for a student in the hostel
    def search_student(self, student_name):
        # Check if the student is in the hostel
        for student in self.students:
            if student.name == student_name:
                print(f"{student_name} is in {self.name}.")
                return
        print(f"{student_name} is not in {self.name}.")


class Student:
    # Initialize the Student object with name and room number
    def __init__(self, name, room_no):
        self.name = name  # Name of the student
        self.room_no = room_no  # Room number of the student


def get_hostel_details():
    name = input("Enter hostel name: ")  # Get the name of the hostel from the user
    capacity = int(input("Enter hostel capacity: "))  # Get the capacity of the hostel from the user
    return name, capacity


def get_student_details():
    name = input("Enter student name: ")  # Get the name of the student from the user
    room_no = int(input("Enter student room number: "))  # Get the room number of the student from the user
    return name, room_no


if __name__ == "__main__":
    hostel_name, hostel_capacity = get_hostel_details()  # Get hostel details from the user
    boys_hostel = Hostel(hostel_name, hostel_capacity)  # Create a Hostel object with the given details

    while True:
        print("\nHostel Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. List Students")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Get user's choice

        if choice == '1':  # If the choice is to add a student
            student_name, student_room_no = get_student_details()  # Get student details from the user
            student = Student(student_name, student_room_no)  # Create a Student object with the given details
            boys_hostel.add_student(student)  # Add the student to the hostel
        elif choice == '2':  # If the choice is to remove a student
            student_name = input("Enter the name of the student you want to remove: ")  # Get the name of the student to be removed
            boys_hostel.remove_student(student_name)  # Remove the student from the hostel
        elif choice == '3':  # If the choice is to list students
            boys_hostel.list_students()  # List all students in the hostel
        elif choice == '4':  # If the choice is to search for a student
            student_name = input("Enter the name of the student you want to search for: ")  # Get the name of the student to search for
            boys_hostel.search_student(student_name)  # Search for the student in the hostel
        elif choice == '5':  # If the choice is to exit
            print("Exiting Hostel Management System. Goodbye!")  # Print exit message
            break  # Exit the loop
        else:  # If the choice is invalid
            print("Invalid choice. Please enter a valid option.")  # Print error message
