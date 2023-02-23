"""
Create a class named student & declare variables name, age, class, rollnumber and inherit the properites to a derived class named marks
and declare a dictionary ehich stores marks of 5 subjects, name & marks and inherit to a class named ReportCard
and access all the variables declared in the super class student from dictionary & print the reuslts with all other details.
"""
class Student:
    def __init__(self, name, age, class_, rollnumber):
        self.name = name
        self.age = age
        self.class_ = class_
        self.rollnumber = rollnumber

class Marks(Student):
    def __init__(self, name, age, class_, rollnumber, marks_dict):
        super().__init__(name, age, class_, rollnumber)
        self.marks_dict = marks_dict

class ReportCard(Marks):
    def __init__(self, name, age, class_, rollnumber, marks_dict):
        super().__init__(name, age, class_, rollnumber, marks_dict)

    def print_report_card(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Class: ', self.class_)
        print('Roll Number: ', self.rollnumber)
        print('~ Grades ~')
        for subject, marks in self.marks_dict.items():
            print(f"{subject}: {marks}")

ishav_dict = {
    "C": 90,
    "Pyhton": 85,
    "AI": 95,
    "ML": 90,
    "DL": 95,
}

report_card = ReportCard(
    name="Ishav Verma",
    age=20,
    class_="6th Sem",
    rollnumber="2020a1r160",
    marks_dict=ishav_dict,
)
report_card.print_report_card()