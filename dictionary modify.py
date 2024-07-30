#Dictionary in python
a = {"name" : "Sajin", "age" :21 , "Gender":"male"}
print(a.values())
#O/P - dict_values(['Sajin', 21, 'male'])
a["age"] = 20
a["skill"] = "python"
print(a)
#After modify - {'name': 'Sajin', 'age': 20, 'Gender': 'male'}
#{'name': 'Sajin', 'age': 20, 'Gender': 'male', 'skill': 'python'}

#update
a.update({"age":10})
print(a)
#After update
#{'name': 'Sajin', 'age': 10, 'Gender': 'male', 'skill': 'python'}
del a["Gender"]
print(a)
# O/P {'name': 'Sajin', 'age': 10, 'skill': 'python'}
a.clear()
print(a) #O/P - {} VALUES ARE CLEARED
del a
print(a)
# O/P - NameError: name 'a' is not defined WE DELECTED COMPLETELY