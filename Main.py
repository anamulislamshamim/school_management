from School import ClassRoom, School
from Persons import Student


def main():
    school = School("Udayan", "Fular road")

    eight = ClassRoom('eight')
    school.add_classroom(eight) 
    nine = ClassRoom('nine')
    school.add_classroom(nine) 
    ten = ClassRoom('ten')
    school.add_classroom(ten) 

    sakib = Student('Sakib Khan', eight)
    school.student_admission(sakib)

    print(school)

if __name__ == "__main__":
    main()