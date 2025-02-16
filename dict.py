# dict
dict1={}
dict2={'jan': '31',
        'feb':'28',
       'march':'31'
}
print(dict1,dict2)
# access dict 
print(dict2['feb'])
# triversal in dict 
for a in dict2:
    print(a,':',dict2[a])
    print(a)
#  itrate over dict
print(dict2.keys())
print(dict2.values())
# muteable dict
dict2['feb']=29
print(dict2)
# eg explain
employee=dict(name='unnat', salary='5,00,00,000', age=12)
print(employee)
# adding element to a dict
employee['deppartment']='sales'
print(employee)
employee['salary']=100000000000000
print(employee)
# nested dict
student={
    'unnat':{'age':12, 'standered':7},
    'gaurav':{'age':12, 'standered':7},
    'avinash':{'age':12, 'standered':7},
    'raghav':{'age':12, 'standered':7}
}
# adding element to nested dict
student['avinash']['age']=4
print(student)
# length of dict
b=len(student)
print(b)
# deleting element in nested dict
del student['avinash']
print(student)
# pop 
student.pop('raghav')
print(student)
# in or not in 
print('avinash' not in student)
for y in student:
    print('student',y,':')
    print('age :',str(student[y]['age']))
    print('standered :',str(student[y]['standered']))
# clear function
dict3=statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
dict3.clear()
print(dict3)
# get()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# items()
print(car.items())
# keys()
print(car.keys())
print(car.values())
car1 = {
  "brand": "mahindra",
  "model": "thar",
  "year": 2023
}
car.update(car1)
print(car,car1)
