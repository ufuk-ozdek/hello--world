num = 5
num *= 4
print(num)
x = -24
print(abs(x))
y = 17.8352
print(round(y))
print(round(y, 2))

print(5 == 6)
print(5 != 6)
num1 = '234'
num2 = '345'
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

num3 = 34
num3 = str(num3)
print(num3 + 'castle')

courses = ['Math', 'Physics', 'CompSci', 'History']
print(courses[0])

courses.append('Art')

print(courses)

courses.insert(0, 'Geography')

print(courses)

courses_2 = ['Geometry', 'Biology']

courses.extend(courses_2)

print(courses)

courses.remove('Math')

print(courses)

popped = courses.pop(0)

print(courses)

print(popped)
'''
for course in courses:
    if 'History' in courses:
        courses.pop()
    else:
        print(courses)
'''
languages = ['Python', 'Java', 'C++', 'French', 'C']
return_value = languages.pop(3)
print('Return Value:', return_value)
print('Updated List:', languages)

print(courses.index('Art', 2))
index = courses.index('Geometry')
print('The index of geometry :', index)

sourted_courses = sorted(courses)
print(sourted_courses)

print('Chemistry' in courses)
print('CompSci' in courses)

for index, item in enumerate(courses, start=1):
    print(index, item)

text = 'Love the neighbor'

print(text.split())

grocery = 'Milk, Chicken, Bread'

print(grocery.split(', '))

print(grocery.split('x'))

dictionary = {"Computer": "Bilgisayar", "Driver": "Sürücü", "Memory": "Hafıza",
              "Output": "Çıktı", "Software": "Yazılım", "Printer": "Yazıcı"}

print(dictionary.keys())

programs = "Python*Java*Ruby*C#"
print(programs.split("*"))

for x in enumerate("ufuk", start=1):
    print(x)

grocery_2 = ['bread', 'milk', 'butter']

for count, item in enumerate(grocery_2):
    print(count, item)

student = {'name': 'Ufuk', 'age': '19', 'classes': ['Math', 'CompSci'], 'gender': 'male'}
print(student.get('phone', 'Error'))
student['phone'] = '5469377807'
print(student.get('phone', 'Error'))
print(student)

student.update({'name': 'John', 'age': '21'})
print(student)

print(len(student))

for x in student:
    print(x)
print()
for a, b in student.items():
    print(a, b)

del student['age']
gender = student.pop('gender')

print(student)
print(gender)


language = 'JavaScript'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No Match')


user = 'Admin'
logged_in = True
if user == 'Admin' or logged_in:
    print('Welcome')
else:
    print('Please log in')


u = [1,2,3]
f = [1,2,3]

print(u is f)
print(u == f)
print(id(f))
print(id(u))


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


condition = 0
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')


nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)
print()
for num in nums:
    if num == 3:
        print('Found!')
    else:
        print(num)
print()
for num in nums:
    if num == 3:
        print('Found!')
    print(num)
print()
q = 0
# while = olduğu zaman
while q < 10 :
    q +=1
    print(q)
