class Person:
    """A class to represent a Person.
    
    Attributes:
    name: str
        The name of the person.
    id_: int
        The person's government identification.
    
    Methods:
    display_info()
        Print the name and id of the person
    """

    def __init__(self, name: str, id_: int):
        self.name = name
        self.id_ = id_

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id_}")


class Student(Person):
    """A class to represent a Student(Person).
    
    Attributes:
    name: str
        The name of the student.
    id_: int
        The student's government identification.
    grades: dict
        A dictionary with the subjects and corresponding grades.
    
    Methods:
    add_grade()
        Add a grade to the grades dictionary.
    get_average()
        Calculate the scores average and append it to grades.
    """

    def __init__(self, name: str, id_: int):
        super().__init__(name, id_)
        self.grades = {}   # Store grades as subject_name: score.

    def display_info(self):
        super().display_info()
        print(self.grades)

    def add_grade(self, subject: str, grade: int):
        """Add a grade to the grades dictionary."""
        self.grades[subject] = grade
    
    def get_average(self):
        """Calculate the scores average and append it to grades."""
        if "Average" in self.grades.keys():
            print("Average already calculated.")
        
        else:
            average = sum(self.grades.values()) / len(self.grades)
            self.add_grade("Average", average)


def grade_reporter(student: Student):    # Return a generator to create the report card for a student.

    def subject_grade_generator():
        for subject, grade in student.grades.items():    # Retrieves the key: value of grades.
            yield subject, grade
    
    return subject_grade_generator()


def save_report(student: Student):
    
    file_name = f"{student.name}.txt"
    
    with open(file_name, "wt") as file:
        file.write(f"Grade Report for {student.name}:\n")
        for subject, grade in grade_reporter(student):
            file.write(f"{subject}: {grade}\n")
    
    print(f"Grade report saved to {file_name}")

# Creating student objects

student1 = Student(input("Name: "), int(input("ID: ")))
student2 = Student(input("Name: "), int(input("ID: ")))

# Adding grades
student1.add_grade("Math", 85)
student1.add_grade("Science", 92)

student2.add_grade("Math", 78)
student2.add_grade("English", 88)

# Calculate the average
student1.get_average()

student2.get_average()
 
# Displaying grade reports
for student in (student1, student2):
    reporter = grade_reporter(student)
    print(f"Grade Report for {student.name}:")
    for subject, grade in reporter:
        print(f"{subject}: {grade}")
    print()

print()

# Saving grade reports
save_report(student1)
save_report(student2)