my_set={12,15,20,25,30}
print(my_set)
print(type(my_set))
my_empty_set=set()
print(my_empty_set)
print(type(my_empty_set))
my_set={1,4,2,3,2,3,4}
print(my_set)
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)
my_set.discard(10)
print(my_set)
removed_item=my_set.pop()
print(removed_item)
print(my_set)
my_set.clear()
print(my_set)
my_set={1,2,3}
print(3 in my_set)
print(4 in my_set)
set1={1,2,3,4,4,5}
set2={4,5,6,7}
union_set=set1.union(set2)
print(union_set)
union=set1 | set2
print(union)
intersection_set=set1.intersection(set2)
print(intersection_set)