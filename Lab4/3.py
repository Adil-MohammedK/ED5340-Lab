def findCGPA(obj):
    cgpa = 0
    # print(obj)
    # print(obj['name'], obj['Courses'])
    course = obj['Courses']
    print(course['Course1']['grade'])
    cgpa = (course['Course1']['grade']*course['Course1']['credit'] +
            course['Course2']['grade']*course['Course2']['credit'] +
            course['Course3']['grade']*course['Course3']['credit'] +
            course['Course4']['grade']*course['Course4']['credit'] +
            course['Course5']['grade']*course['Course5']['credit'])/(course['Course1']['credit']+course['Course2']['credit']+course['Course3']['credit']+course['Course4']['credit']+course['Course5']['credit'])
    obj['cgpa'] = cgpa
    print(obj)


def printReport(obj):
    print("")
    print("************** REPORT CARD *******")
    print("Name: ", obj['name'])
    print("Roll: ", obj['roll'])
    print("Courses: ", obj['Courses'])
    print("CGPA: ", obj['cgpa'])


gradeSheet = {'Student1': {'name': 'Adil', 'roll': '41', 'Courses': {
    'Course1': {'grade': 9, 'credit': 12}, 'Course2': {'grade': 10, 'credit': 3}, 'Course3': {'grade': 8, 'credit': 9}, 'Course4': {'grade': 9, 'credit': 10}, 'Course5': {'grade': 9, 'credit': 12}}},
    'Student2': {'name': 'Mohammed', 'roll': '40', 'Courses': {
        'Course1': {'grade': 8, 'credit': 12}, 'Course2': {'grade': 8, 'credit': 3}, 'Course3': {'grade': 9, 'credit': 9}, 'Course4': {'grade': 9, 'credit': 10}, 'Course5': {'grade': 9, 'credit': 12}}},
    'Student3': {'name': 'Malay', 'roll': '42', 'Courses': {
        'Course1': {'grade': 8, 'credit': 12}, 'Course2': {'grade': 9, 'credit': 3}, 'Course3': {'grade': 10, 'credit': 9}, 'Course4': {'grade': 7, 'credit': 10}, 'Course5': {'grade': 10, 'credit': 12}}}}

# print(gradeSheet)
for obj in gradeSheet:
    # print(obj, gradeSheet[obj])
    findCGPA(gradeSheet[obj])

query = input('Enter name of student to show report Card:')
for obj in gradeSheet:
    if gradeSheet[obj]['name'] == query:
        printReport(gradeSheet[obj])
