


class Student(object):
    def __init__(self, name):
        self.name =name
    def __str__(self):
        return f'Student object {self.name}'


print(Student('cc'))
s= Student('HH')
print(s)