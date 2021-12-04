School = {}
for i in range(3):
    School.update({input('Название класса: '): int(input('Количество учеников: '))})
print(School)
for i in range(1):
    School.update({input('Название изменяемого класса: '): int(input('Количество учеников: '))})
print(School)
for i in range(1):
    School.update({input('Название нового класса: '): int(input('Количество учеников: '))})
print(School)
del School[input('Название удаляемого класса: ')]
print(School)
AllSchool = sum(School.values())
print(AllSchool)
