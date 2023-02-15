import StudentClass as sc

def main():

    stu_id = 101
    name = 'Braeden'
    dob = "06/26/2000"
    classification = "senior"

    student1 = sc.Student(stu_id, name, dob, classification)

    student1.calc_age()
    student1.calc_register()

    print(f"Student age is: {student1.get_age()}")
    print(f"Student can register between: {student1.get_register()}")

main()

