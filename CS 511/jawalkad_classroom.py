class Student():
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.assignments = []

    def get_id(self):
        return self.id

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_assignments(self):
        return self.assignments

    def get_assignment(self, name):
        for assignment in self.assignments:
            if(assignment.name==name):
                return assignment.grade
        return None

    def get_average(self):
        grade_sum = 0 
        count = 0
        for assignment in self.assignments:
            if(assignment.grade):
                grade_sum += assignment.grade
                count += 1

        return grade_sum/count

    def submit_assignment(self, assignment):
        self.assignments.append(assignment)

    def remove_assignment(self, name):
        for assignment in self.assignments:
            if(assignment.name==name):
                self.assignments.remove(assignment)
                break

class Assignment():
    def __init__(self, name, max_score):
        self.name = name
        self.max_score = max_score
        self.grade = None

    def assign_grade(self, grade):
        if(grade<=self.max_score):
            self.grade = grade

