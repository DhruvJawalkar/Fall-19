from jawalkad_classroom import Student, Assignment

def main():
    allen = Student(123, "Allen", "Anderson")
    becky = Student(456, "Becky", "Beckyson")

    print(allen.get_full_name()+',', "id:", allen.get_id())
    print(becky.get_full_name()+',', "id:", becky.get_id())

    a11 = Assignment("Assignment 1", 100)
    a12 = Assignment("Assignment 1", 100)
    a21 = Assignment("Assignment 2", 100)
    a22 = Assignment("Assignment 2", 100)

    a11.assign_grade(75)
    a21.assign_grade(85)
    allen.submit_assignment(a11)
    allen.submit_assignment(a21)

    a12.assign_grade(90)
    a22.assign_grade(100)
    becky.submit_assignment(a12)
    becky.submit_assignment(a22)

    print("Assignment 1 grade for "+allen.get_full_name()+" : "+ str(allen.get_assignment("Assignment 1")))
    print("Assignment 1 grade for "+becky.get_full_name()+" : "+ str(becky.get_assignment("Assignment 1")))

    beckys_assignments = becky.get_assignments()
    print("Becky's assignment grades: ")
    for assignment in beckys_assignments:
        print(assignment.name, " : ", assignment.grade)

    print("Average grade for Becky: ", becky.get_average())

    becky.remove_assignment("Assignment 2")
    print("Removed Assignment 2 for Becky")

    print("Average grade for Becky: ", becky.get_average())


if __name__=="__main__":
    main()