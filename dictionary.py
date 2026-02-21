empty_dict={}
print(empty_dict)
print(type(empty_dict))
my_dict={"name":"Alice","age":30,"city":"New York"}
print(my_dict)
empty_dict=dict()
print(empty_dict)
print(type(empty_dict))
my_dict={"name":"Alice","age":30,"city":"New York", "name":"Bob"}
print(my_dict)
my_dict["age"]=31
print(my_dict)
print(my_dict["name"])
print(my_dict.get("name"))
print(my_dict.get("country","USA"))
print(my_dict.get("last_name"))
print(my_dict.get("last_name","Smith"))
my_dict["country"]="USA"
print(my_dict)
del my_dict["city"]
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict.clear()
print(my_dict)
my_dict={"name":"Alice","age":30,"city":"New York"}
print("name" in my_dict)
print("country" in my_dict)
print(my_dict.keys())
print(my_dict.values()) 
print(my_dict.items())
my_dict_copy=my_dict
print(my_dict_copy)
print(my_dict_copy is my_dict)
my_dict_copy["age"]=31  
print(my_dict)
my_dict_copy=my_dict.copy()
print(my_dict_copy)

my_dict_copy["age"]=33
print(my_dict)
print(my_dict_copy)
for key in my_dict:
    print(key)
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(f"{key}: {value}")
students={"student1":{"name":"Alice","age":20,"major":"Computer Science"},
          "student2":{"name":"Bob","age":22,"major":"Mathematics"}    }
print(students)
print(students["student1"])
print(students["student1"]["name"])
print(students["student2"])
print(students["student2"]["name"])
print(students.items())
for student_id, student_info in students.items():
    print(f"{student_id}: {student_info}")
    for key, value in student_info.items():
        print(f"  {key}: {value}")
