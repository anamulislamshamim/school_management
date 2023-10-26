class School:
    def __init__(self, name, address) -> None:
        self.name = name 
        self.address = address 
        self.class_rooms = {}
        self.teachers = {}
    
    def add_teacher(self, teacher, subject):
        if subject in self.teachers:
            self.teachers[subject].append(teacher)
        else:
            self.teachers[subject] = [teacher]

    def add_classroom(self, classroom):
        self.class_rooms[classroom.name] = []
    
    def student_admission(self, student):
        print("I visited!")
        classroom = student.classroom
        if classroom in self.class_rooms:
            # TODO: set student id
            self.class_rooms[classroom].append(student)
        else:
            print(f"No classroom available as named {classroom}")
    
    def __repr__(self) -> str:
        for key, val in self.class_rooms.items():
            print(f"{key}")
        print(len(self.class_rooms['eight']))
        return ""


class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name 
        self.students = []
    
    def add_student(self, student):
        serial_id = f'{self.name}-{len(self.students)}'
        self.students.append(student)
        student.id = serial_id 
    
    def __repr__(self) -> str:
        return f"{self.name}-{len(self.students)}"

    def get_top_students(self):
        # TODO: sort students by grade 
        pass 


class Subject:
    def __init__(self, name) -> None:
        self.name = name 
        self.max_mark = 100
        self.min_mark = 40
