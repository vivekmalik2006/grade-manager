"""
Simple Grade Manager System
A basic program to manage student grades - Perfect for first-year B.Tech project
"""

import json
import os
from datetime import datetime

class Student:
    """Simple Student class"""
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}  # Dictionary to store subject: marks
    
    def add_marks(self, subject, marks):
        """Add marks for a subject"""
        self.marks[subject] = marks
        print(f"Marks added for {subject}")
    
    def calculate_percentage(self):
        """Calculate overall percentage"""
        if not self.marks:
            return 0
        total = sum(self.marks.values())
        return total / len(self.marks)
    
    def get_grade(self, percentage):
        """Convert percentage to grade"""
        if percentage >= 90:
            return 'A+'
        elif percentage >= 80:
            return 'A'
        elif percentage >= 70:
            return 'B'
        elif percentage >= 60:
            return 'C'
        elif percentage >= 50:
            return 'D'
        else:
            return 'F'
    
    def display_info(self):
        """Display student information"""
        print(f"\n{'='*40}")
        print(f"Student: {self.name} (Roll No: {self.roll_no})")
        print(f"{'='*40}")
        
        if self.marks:
            print("\nMarks:")
            for subject, marks in self.marks.items():
                print(f"  {subject}: {marks}")
            
            percentage = self.calculate_percentage()
            grade = self.get_grade(percentage)
            print(f"\nPercentage: {percentage:.2f}%")
            print(f"Grade: {grade}")
        else:
            print("No marks added yet")
        
        print(f"{'='*40}")

class GradeManager:
    """Main Grade Manager Class"""
    def __init__(self):
        self.students = {}
        self.filename = "student_data.json"
        self.load_data()
    
    def load_data(self):
        """Load data from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    for roll_no, student_data in data.items():
                        student = Student(roll_no, student_data['name'])
                        student.marks = student_data['marks']
                        self.students[roll_no] = student
                print(f"Loaded {len(self.students)} students from file")
            except:
                print("No previous data found or error loading data")
    
    def save_data(self):
        """Save data to file"""
        data = {}
        for roll_no, student in self.students.items():
            data[roll_no] = {
                'name': student.name,
                'marks': student.marks
            }
        
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully!")
    
    def add_student(self):
        """Add a new student"""
        print("\n--- Add New Student ---")
        roll_no = input("Enter Roll Number: ").strip()
        
        if roll_no in self.students:
            print("Student with this roll number already exists!")
            return
        
        name = input("Enter Student Name: ").strip()
        self.students[roll_no] = Student(roll_no, name)
        print(f"Student {name} added successfully!")
        self.save_data()
    
    def add_marks(self):
        """Add marks for a student"""
        print("\n--- Add Marks ---")
        roll_no = input("Enter Roll Number: ").strip()
        
        if roll_no not in self.students:
            print("Student not found!")
            return
        
        student = self.students[roll_no]
        print(f"Adding marks for {student.name}")
        
        subject = input("Enter Subject Name: ").strip()
        
        try:
            marks = float(input("Enter Marks (out of 100): ").strip())
            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100")
                return
        except ValueError:
            print("Invalid marks! Please enter a number.")
            return
        
        student.add_marks(subject, marks)
        self.save_data()
    
    def view_student(self):
        """View a specific student's details"""
        print("\n--- View Student Details ---")
        roll_no = input("Enter Roll Number: ").strip()
        
        if roll_no not in self.students:
            print("Student not found!")
            return
        
        self.students[roll_no].display_info()
    
    def view_all_students(self):
        """View all students"""
        print("\n--- All Students ---")
        if not self.students:
            print("No students added yet")
            return
        
        for student in self.students.values():
            print(f"\nRoll No: {student.roll_no}, Name: {student.name}")
            if student.marks:
                avg = student.calculate_percentage()
                print(f"  Subjects: {len(student.marks)}, Average: {avg:.2f}%")
    
    def generate_report(self):
        """Generate class report"""
        print("\n=== CLASS REPORT ===")
        print(f"Total Students: {len(self.students)}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("="*30)
        
        if not self.students:
            print("No students to generate report")
            return
        
        # Calculate class statistics
        all_percentages = []
        for student in self.students.values():
            if student.marks:
                all_percentages.append(student.calculate_percentage())
        
        if all_percentages:
            print(f"\nClass Average: {sum(all_percentages)/len(all_percentages):.2f}%")
            print(f"Highest: {max(all_percentages):.2f}%")
            print(f"Lowest: {min(all_percentages):.2f}%")
        
        # Show toppers
        print("\nTop 3 Students:")
        students_with_avg = [(s.name, s.calculate_percentage()) 
                           for s in self.students.values() if s.marks]
        students_with_avg.sort(key=lambda x: x[1], reverse=True)
        
        for i, (name, avg) in enumerate(students_with_avg[:3], 1):
            print(f"  {i}. {name} - {avg:.2f}%")
        
        print("="*30)
    
    def delete_student(self):
        """Delete a student"""
        print("\n--- Delete Student ---")
        roll_no = input("Enter Roll Number to delete: ").strip()
        
        if roll_no in self.students:
            name = self.students[roll_no].name
            confirm = input(f"Delete {name}? (yes/no): ").strip().lower()
            if confirm == 'yes':
                del self.students[roll_no]
                print(f"Student {name} deleted!")
                self.save_data()
            else:
                print("Deletion cancelled")
        else:
            print("Student not found!")
    
    def show_menu(self):
        """Display menu"""
        print("\n" + "="*40)
        print("      SIMPLE GRADE MANAGER")
        print("="*40)
        print("1. Add New Student")
        print("2. Add Marks for Student")
        print("3. View Student Details")
        print("4. View All Students")
        print("5. Generate Class Report")
        print("6. Delete Student")
        print("7. Exit")
        print("="*40)
    
    def run(self):
        """Main program loop"""
        print("Welcome to Simple Grade Manager!")
        print("Created for B.Tech First Year Project")
        
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_marks()
            elif choice == '3':
                self.view_student()
            elif choice == '4':
                self.view_all_students()
            elif choice == '5':
                self.generate_report()
            elif choice == '6':
                self.delete_student()
            elif choice == '7':
                print("\nThank you for using Grade Manager!")
                print("Saving data...")
                self.save_data()
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-7")

# Main program entry point
if __name__ == "__main__":
    # Create and run the grade manager
    manager = GradeManager()
    manager.run()