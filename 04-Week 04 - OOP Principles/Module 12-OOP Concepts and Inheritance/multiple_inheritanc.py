
#! Multiple inheritance with school students and sports

class School:
    def __init__(self,school_name) -> None:
        self.school_name = school_name
        print("School init called")

class Grade:
    def __init__(self,grade_name) -> None:
        self.grade_name = grade_name
        print("Grade class init called")

class Student(School,Grade):
    def __init__(self, name, grade_name, school_name) -> None:
        self.name = name
        print("Student init called")
        Grade.__init__(self,grade_name)
        School.__init__(self,school_name)

hamid_h = Student("AJ","MBA","Uk School")
print(hamid_h.name)
print(hamid_h.school_name)
print(hamid_h.grade_name)