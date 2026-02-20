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
