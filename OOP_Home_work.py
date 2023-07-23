class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


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
        average_rating = b / len(a)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {round(average_rating, 2)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
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

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}
    def __str__(self):
        a = []
        b = 0
        for key in self.grades.values():
            for i in key:
                b += i
                a.append(i)
        average_rating = b / len(a)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(average_rating, 2)}\n'
        return res
    pass
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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'GIT']

cool_Rewiewer = Rewiewer('Some', 'Buddy')
cool_Rewiewer.courses_attached += ['Python']

cool_Rewiewer.rate_hw(best_student, 'Python', 10)
cool_Rewiewer.rate_hw(best_student, 'Python', 7)
cool_Rewiewer.rate_hw(best_student, 'Python', 9)

# print(best_student.grades)

# Задание 2
cool_Lecturer = Lecturer('Someone', 'Someone-else')
cool_Lecturer.courses_attached += ['Python']
best_student.rate_lector(cool_Lecturer, 'Python', 9)
best_student.rate_lector(cool_Lecturer, 'Python', 8)
best_student.rate_lector(cool_Lecturer, 'Python', 7)
best_student.rate_lector(cool_Lecturer, 'Python', 9)

# print(cool_Lecturer.grades)

# задание 3
best_student.finished_courses += ['Some course #1', 'Some course #2']
print(cool_Rewiewer)
print(cool_Lecturer)
print(best_student)
