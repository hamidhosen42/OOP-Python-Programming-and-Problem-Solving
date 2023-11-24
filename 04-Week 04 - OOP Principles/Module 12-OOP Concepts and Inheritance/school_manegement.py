import time

class School:

    # ! constructor
    def __init__(self, name, location,principle=''):
        self.name = name
        self.location = location
        self.principle = principle
        self.grades = []

    def add_grade(self,name,teacher):
        new_grade = Grade(name,teacher)
        self.grades.append(new_grade)

    def remove_grade(self,name):
        idx = 0
        for i,grade in enumerate(self.grades):
            if grade.name == name:
                idx = i
                break
        del self.grades[idx]

class Grade:

    # ! constructor
    def __init__(self,name,teacher) -> None:
        self.student = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'class of {self.name} with teacher {self.teacher}'
    
    # !destructor
    def __del__(self):
  	  print(f"Deleting {self.name} class {self.teacher}")


edu = School("EDU","Dhaka","Hamid")
edu.add_grade("class 3","Dr.Hamid")
edu.add_grade("class 4","Dr.Hamid Hosen")
edu.add_grade("class 5","Dr.Hamid Hosen")

print(edu.grades)
edu.remove_grade("class 3")
print(edu.grades)

print("My code running is done")
time.sleep(5)