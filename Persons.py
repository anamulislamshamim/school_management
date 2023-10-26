import random


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject
    
    def teach(self):
        pass 
    
    def take_exam(self, subject, students):
        for student in students:
            marks = random.randint(0, 100)
            # TODO: set marks for the subject for each students


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.subjects = []
        self.__id = None 
        self.classroom = classroom.name
        self.marks = {}
        self.grade = None 
    
    @property
    def id(self):
        return self.__id 
    
    @id.setter
    def id(self, val):
        self.__id = val 
    

