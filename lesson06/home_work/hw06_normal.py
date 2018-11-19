# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, name, surname, familyname):
        self.name = name
        self.surname = surname
        self.familyname = familyname

    @property
    def fullname(self):
        return '{} {} {}'.format(self.familyname, self.name, self.surname)

    @property
    def shortname(self):
        return '{} {}.{}.'.format(self.familyname, self.name[0], self.surname[0])


class Student(Person):
    def __init__(self, name, surname, familyname, father, mother, school_class):
        super().__init__(name, surname, familyname)
        self.father = father
        self.mother = mother
        self.school_class = school_class

    def get_parents(self):
        return self.father.shortname, self.mother.shortname

class Teacher(Person):
    def __init__(self, name, surname, familyname, subject):
        super().__init__(name, surname, familyname)
        self.subject = subject


class School_class:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    @property
    def subjlist(self):
        return [s.subject for s in self.subjects]

    @property
    def teacherslist(self):
        return [s.shortname for s in self.subjects]


class School:
    def __init__(self):
        self.classes = []
        self.students = []
        self.teachers = []

    def find_class(self, cl_name):
        for cl in self.classes:
            if cl.name == cl_name:
                return cl
        return 0

    def add_class(self, classname):
        if not self.find_class(classname):
            self.classes.append(School_class(classname))

    @property
    def classeslist(self):
        return [c.name for c in self.classes]

    def find_student(self, name, surname, familyname):
        for st in self.students:
            if st.name == name and st.surname == surname and st.familyname == familyname:
                return st
        return 0

    def find_students(self, classname):
        studentslist = []
        cl = self.find_class(classname)
        if cl:
            for student in self.students:
                if student.school_class == cl:
                    studentslist.append(student.shortname)
        return studentslist

    def add_student(self, name, surname, familyname, father, mother, school_class):
        stud = Student(name, surname, familyname, father, mother, school_class)
        if stud:
            self.students.append(stud)
        return stud

    def find_teacher(self, subj):
        for t in self.teachers:
            if t.subject == subj:
                return t
        return 0

    def add_teacher(self,  name, surname, familyname, subject):
        t = self.find_teacher(subject)
        if not t:
            t = Teacher(name, surname, familyname, subject)
            self.teachers.append(t)
            return t
        else:
           return 0

    def add_subject(self, cl_name, subject):
        t = self.find_teacher(subject)
        cl = self.find_class(cl_name)
        cl.subjects.append(t)


school = School()

school.add_class('1a')
school.add_class('1b')
school.add_class('1c')

father = Person('fav','fav','fav')
mother = Person('mom','mom','mom')
school.add_student('name','sur','fam',father,mother, school.find_class('1b'))
school.add_student('Иван', 'Иванович', 'Иванов', Person('father1', 'fatherson', 'Father1'),
                   Person('mother1', 'Motherson', 'Mother1'), school.find_class('1a'))
school.add_student('Иван2', 'Иванович2', 'Иванов2', Person('father2', 'fatherson2', 'Father2'),
                   Person('mother2', 'Motherson2', 'Mother2'), school.find_class('1a'))
school.add_student('Иван3', 'Иванович3', 'Иванов3', Person('father3', 'fatherson3', 'Father3'),
                   Person('mother3', 'Motherson3', 'Mother3'), school.find_class('1b'))
school.add_student('Иван4', 'Иванович4', 'Иванов4', Person('father4', 'fatherson4', 'Father4'),
                   Person('mother4', 'Motherson4', 'Mother4'), school.find_class('1b'))
school.add_student('Иван5', 'Иванович5', 'Иванов5', Person('father5', 'fatherson5', 'Father5'),
                   Person('mother5', 'Motherson5', 'Mother5'), school.find_class('1c'))
school.add_student('Иван6', 'Иванович6', 'Иванов6', Person('father6', 'fatherson6', 'Father6'),
                   Person('mother6', 'Motherson6', 'Mother6'), school.find_class('1c'))

print('Список классов:')
print(school.classeslist)

print('ученики 1а класса:')
print(school.find_students("1a"))
print('ученики 1b класса:')
print(school.find_students("1b"))
print('ученики 1c класса:')

print(school.find_students("1c"))
print('родители ученика Иван Иванович Иванов:', school.find_student('Иван', 'Иванович', 'Иванов').get_parents())

school.add_teacher('Математик', 'Мат', 'Мат', 'математика')
school.add_teacher('Физрук', 'Физрукови', 'Физруков', 'физра')
school.add_teacher('Язык', 'Языкови', 'Языков', 'языки')

school.add_subject('1a','физра')
school.add_subject('1a','математика')
school.add_subject('1b','языки')
school.add_subject('1b','языки')
school.add_subject('1c','физра')
school.add_subject('1c','математика')
school.add_subject('1c','языки')


print('список предметов ученика Иван Иванович Иванов:', school.find_student('Иван', 'Иванович', 'Иванов').school_class.subjlist)
print('список преподающих в 1с классе:', school.find_class('1c').teacherslist)

