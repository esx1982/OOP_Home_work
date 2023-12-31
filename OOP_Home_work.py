class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
# задание 3
    def __str__(self):
        a = []
        b = 0
        for key in self.grades.values():
            for i in key:
                b += i
                a.append(i)
        self.average_rating = b / len(a)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(self.average_rating, 2)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

#задание 2
    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

student_list = ["student_1", "student_2"]

# def student_average_rating(student_list, course):
#     for name in student_list:
#         print(getattr(name, 'grades'))



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = 0
        self.student_list = []

class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        a = []
        b = 0
        for key in self.grades.values():
            for i in key:
                b += i
                a.append(i)
        self.average_rating = b / len(a)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average_rating, 2)}\n'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
        return self.average_rating < other.average_rating

class Rewiewer(Mentor):
# Задание 2
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python', 'GIT']
#
# cool_Rewiewer = Rewiewer('Some', 'Buddy')
# cool_Rewiewer.courses_attached += ['Python']
#
# cool_Rewiewer.rate_hw(best_student, 'Python', 10)
# cool_Rewiewer.rate_hw(best_student, 'Python', 7)
# cool_Rewiewer.rate_hw(best_student, 'Python', 9)

# print(best_student.grades)

# Задание 2
# cool_Lecturer = Lecturer('Someone', 'Someone-else')
# cool_Lecturer.courses_attached += ['Python']
# best_student.rate_lector(cool_Lecturer, 'Python', 9)
# best_student.rate_lector(cool_Lecturer, 'Python', 8)
# best_student.rate_lector(cool_Lecturer, 'Python', 7)
# best_student.rate_lector(cool_Lecturer, 'Python', 9)

# print(cool_Lecturer.grades)

# задание 3
# best_student.finished_courses += ['Some course #1', 'Some course #2']
# print(cool_Rewiewer)
# print(cool_Lecturer)
# print(best_student)
# print(cool_Lecturer < best_student)

# задание 4
student_1 = Student('Maksim', 'Petrov', 35)
student_1.courses_in_progress += ['Python', 'GIT']
student_1.finished_courses += ['Some course']
student_2 = Student('Evgeniy', 'Fedorov', 25)
student_2.courses_in_progress += ['Python', 'GIT']
student_2.finished_courses += ['Some course']

rewiewer_1 = Rewiewer('Aleksand', 'Ivanov')
rewiewer_1.courses_attached += ['Python']
rewiewer_2 = Rewiewer('Maria', 'Tesnova')
rewiewer_2.courses_attached += ['GIT']
rewiewer_1.rate_hw(student_1, 'Python', 9)
rewiewer_1.rate_hw(student_1, 'Python', 8)
rewiewer_1.rate_hw(student_2, 'Python', 10)
rewiewer_1.rate_hw(student_2, 'Python', 9)
rewiewer_2.rate_hw(student_1, 'GIT', 8)
rewiewer_2.rate_hw(student_1, 'GIT', 10)
rewiewer_2.rate_hw(student_2, 'GIT', 9)
rewiewer_2.rate_hw(student_2, 'GIT', 10)

lecturer_1 = Lecturer('Aleksey', 'Belov')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Elena', 'Shatova')
lecturer_2.courses_attached += ['GIT']

student_1.rate_lector(lecturer_1, 'Python', 9)
student_2.rate_lector(lecturer_1, 'Python', 8)
student_1.rate_lector(lecturer_2, 'GIT', 10)
student_2.rate_lector(lecturer_2, 'GIT', 9)

print(student_1.grades)
print(student_2.grades)
print(lecturer_1.grades)
print(lecturer_2.grades)
print(rewiewer_1)
print(rewiewer_2)
print(student_1)
print(student_2)
print(lecturer_1 < student_1)
print(lecturer_2 < student_2)

# задание 4
student_list = [student_1, student_2]

def student_average_rating(student_list, course):
    a = []
    b = 0
    for name in student_list:
        if course in name.grades:
            for i in name.grades[course]:
                b += i
                a.append(i)
    av_rating = b / len(a)
    print(f'средняя оценка: {av_rating} за домашние задания по всем студентам в рамках курса "{course}"')
student_average_rating(student_list, 'GIT')
student_average_rating(student_list, 'Python')

lecturer_list = [lecturer_1, lecturer_2]

def lecturer_average_rating(lecturer_list, course):
    a = []
    b = 0
    for name in lecturer_list:
        if course in name.grades:
            for i in name.grades[course]:
                b += i
                a.append(i)
    av_rating = b / len(a)
    print(f'средняя оценка: {av_rating} за лекции всех лекторов в рамках курса "{course}"')
lecturer_average_rating(lecturer_list, 'Python')
lecturer_average_rating(lecturer_list, 'GIT')