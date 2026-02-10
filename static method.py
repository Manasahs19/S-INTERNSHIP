class Student:
    # Class variable (shared by all students)
    college_name = "GEC Ramanagara"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print("-" * 20)

    # Class method (updates shared data)
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Static method (helper function)
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"
# Create students
s1 = Student("Manasa", 101)
s2 = Student("Darshu", 102)

# Display details
s1.display()
s2.display()

# Change college name using classmethod
Student.change_college("Gousia College")

# Display again (college name updated for all)
s1.display()
s2.display()

# Check pass/fail using staticmethod
print("Marks 40:", Student.is_pass(40))
print("Marks 20:", Student.is_pass(20))
        
