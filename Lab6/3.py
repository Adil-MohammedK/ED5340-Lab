
class Btech:
    def __init__(self, btStudents=dict()):
        self.btStudents = btStudents
        self.BTcourses = {1: "Course1", 2: "Course2", 3: "Course3"}
        print(self.btStudents)


class DD:
    def __init__(self, students=dict()):
        self.DDStudents = students
        self.DDcourses = {4: "Course4", 5: "Course5", 6: "Course6"}


class MS:
    def __init__(self, students=dict()):
        self.MSStudents = students
        self.MScourses = {7: "Course7", 8: "Course8", 9: "Course9"}
        print(self.MSStudents)


class Phd:
    def __init__(self, students=dict()):
        self.phdStudents = students
        self.PHDcourses = {10: "Course10", 11: "Course11", 12: "Course12"}


class Student:
    def __init__(self, students=dict()):
        self.students = students

    def findStream(self, sname):
        for stud in self.students:
            if stud == sname:
                print("Stream of student is ", self.students[stud]["Stream"])

    def addCourse(self, sname):
        course = []
        course = input("Enter nums of courses keeping space: ").split(" ")
        for stud in self.students:
            if stud == sname:
                for x in course:
                    self.students[stud]["Courses"].add(int(x))
                print(self.students[stud])
                break


class Department(Btech, DD, MS, Phd, Student):
    def __init__(self, student_list):

        # print(isinstance(self.students, Department))
        BtStudents = dict()
        DDStudents = dict()
        MSStudents = dict()
        PhDStudents = dict()
        for student in student_list:
            if student_list[student]["Stream"] == "BTech":
                BtStudents[student] = student_list[student]
            elif student_list[student]["Stream"] == "DD":
                DDStudents[student] = student_list[student]
            elif student_list[student]["Stream"] == "MS":
                MSStudents[student] = student_list[student]
            elif student_list[student]["Stream"] == "PhD":
                PhDStudents[student] = student_list[student]

        # print(DDStudents)
        Student.__init__(self, student_list)
        Btech.__init__(self, BtStudents)
        DD.__init__(self, DDStudents)
        MS.__init__(self, MSStudents)
        Phd.__init__(self, PhDStudents)

    def studDetails(self, sname):
        for stud in self.students:
            if stud == sname:
                print("Name of student: ", stud)
                print("Roll of Student: ", self.students[stud]["Roll"])
                print("Roll of Student: ", self.students[stud]["Stream"])
                print("Courses of Student: ")
                for course in self.students[stud]['Courses']:
                    if self.students[stud]["Stream"] == "BTech":
                        print(self.BTcourses[course])
                    elif self.students[stud]["Stream"] == "DD":
                        print(self.DDcourses[course])
                    elif self.students[stud]["Stream"] == "MS":
                        print(self.MScourses[course])
                    elif self.students[stud]["Stream"] == "PhD":
                        print(self.PHDcourses[course])
                break

    def getCGPA(self):
        for stud in self.students:
            self.students[stud]["CGPA"] = 0.00
            total_points, total_credits = 0, 0
            for x in range(len(self.students[stud]["Credits"])):
                total_points += (self.students[stud]["Credits"]
                                 [x]*self.students[stud]["Points"][x])
                print(self.students[stud]["Credits"][x])
                print(self.students[stud]["Points"][x])

                total_credits += (self.students[stud]["Credits"][x])
            self.students[stud]["CGPA"] = float(total_points)/total_credits


student_list = {"Name1": {"Roll": 1, "Stream": "BTech", "Courses": {1, 2}, "Credits": [9, 8], "Points": [10, 9]},
                "Name2": {"Roll": 2, "Stream": "BTech", "Courses": {1}, "Credits": [8], "Points": [9]},
                "Name3": {"Roll": 3, "Stream": "BTech", "Courses": {1, 3}, "Credits": [12, 8], "Points": [8, 9]},
                "Name4": {"Roll": 4, "Stream": "DD", "Courses": {5, 6}, "Credits": [9, 8], "Points": [9, 9]},
                "Name5": {"Roll": 5, "Stream": "DD", "Courses": {4, 5}, "Credits": [9, 8], "Points": [7, 8]},
                "Name6": {"Roll": 6, "Stream": "DD", "Courses": {4}, "Credits": [9], "Points": [8]},
                "Name7": {"Roll": 7, "Stream": "MS", "Courses": {7, 8}, "Credits": [10, 8], "Points": [8, 9]},
                "Name8": {"Roll": 8, "Stream": "MS", "Courses": {8}, "Credits": [12], "Points": [8, 10]},
                "Name9": {"Roll": 9, "Stream": "PhD", "Courses": {10, 11, 12}, "Credits": [7, 10, 11], "Points": [9, 9, 8]}
                }

ED = Department(student_list)
ED.findStream("Name6")
ED.studDetails("Name5")
ED.addCourse("Name3")
ED.getCGPA()
print(ED.students)
