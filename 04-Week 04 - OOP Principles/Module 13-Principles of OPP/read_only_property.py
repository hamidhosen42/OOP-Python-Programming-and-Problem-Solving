class Student:
    def __init__(self,name,id,marks) -> None:
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def student_id(self):
        return self.__id
    
    @property
    def name(self):
        return self._name
    
    @name.deleter
    def name(self):
        del self._name
    
hamid = Student("Hamid",20,30)
print(hamid.student_id)
print(hamid.name)

del hamid.name
print(dir(hamid))

# hamid.student_id = 23
# print(hamid.student_id)