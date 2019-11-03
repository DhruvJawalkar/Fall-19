
students = [{
    'id' : 12345,
    'first_name' : 'Alice',
    'last_name' : 'Anderson',
    'assignments' : [
        ('assignment_1', 3),
        ('assignment_2', 2),
        ('assignment_3', 4)
    ]
},
{
    'id' : 12344,
    'first_name' : '2Alice',
    'last_name' : '2Anderson',
    'assignments' : [
        ('assignment_1', 0),
        ('assignment_2', 2),
        ('assignment_3', 4)
    ]
}]

def average_grade(students):
    avg = 0
    count = 0
    for student in students:
        for (_, grade) in student['assignments']:
            avg += grade
            count +=1
    return avg/count        

def add_grade(student, assignment_name, grade):
    found = False
    for (a_name, _) in student['assignments']:
        if(assignment_name==a_name):
            found=True
            #student['assignments'][a_name] = grade
    if(not found):
        student['assignments'].append((assignment_name, grade))
    return not found     

def update_grade(student, assignment_name, grade):
    found = False
    for i, (a_name, _) in enumerate(student['assignments']):
        if(assignment_name==a_name):
            found=True
            student['assignments'][i] = (assignment_name,grade)    
    return found 

def highest_n_grades(students, assignment_name, n):
    students.sort(key= lambda x: x['id'])
    grades = []
    for student in students:
        for (a_name, grade) in student["assignments"]:
            if(a_name == assignment_name):
                grades.append(grade)
                
    sorted_indices = [i[0] for i in sorted(enumerate(grades), key=lambda x:x[1], reverse=True)]
    res = []
    for i in range(n):
        res.append(students[sorted_indices[i]])  
    return res     

def passing_student_ids(students):
    ids = []
    for student in students:
        abv_avg = True
        for (_, grade) in student['assignments']:
            if(grade<2):
                abv_avg = False
                break   
        if(abv_avg):     
            ids.append(student['id'])
    return ids
