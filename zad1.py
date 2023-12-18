class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0
        return average_marks > 50

student1 = Student("John", [60, 70, 80])
student2 = Student("Alice", [40, 30, 20])

print(f"{student1.name} is passed: {student1.is_passed()}")
print(f"{student2.name} is passed: {student2.is_passed()}")