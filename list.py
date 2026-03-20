lst=[]
print(type(lst))
name=["John","Alice","Bob",1,3.14]
print(name)
print(name[0])
mixed_list=[1,"Hello",3.14,True]
print(mixed_list)
print(mixed_list[1])
print(mixed_list[-1])
fruits=["apple","banana","cherry"]  
print(fruits[0:2])
print(fruits[1:])
print(fruits[:2])
fruits.append("orange")
print(fruits)
fruits.insert(1,"grape")
print(fruits)
fruits[1]="kiwi"
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.remove("orange")
print(fruits)
fruits.pop()
print(fruits)
fruits.index("kiwi")
print(fruits.index("kiwi"))
fruits.insert(2,"melon")
print(fruits)
print(len(fruits))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.clear()
print(fruits) 
numbers=[5,2,9,1,5,6]
print(numbers[::-1]) 
numbers.sort()
print(numbers)
print(numbers[1:4]) 
lst1=[]
for i in range(5):
    lst1.append(i*2)
print(lst1)
squares=[x**2 for x in range(10)]
print(squares)
cubes=[x**3 for x in range(10)]
print(cubes)
even_numbers=[x for x in range(20) if x%2==0]
print(even_numbers)
odd_numbers=[x for x in range(20) if x%2!=0]
print(odd_numbers)
list2=[12,15,20,25,30]
list3=["a","b","c","d","e"]
pair=[(x,y) for x in list2 for y in list3]
print(pair)
words=["hello","world","python","programming"]
lengths=[len(word) for word in words]
print(lengths)
print(type(lengths))
list4=['baij','uday','adu','prema']
list5=['husband','first_son','second_son','wife']
pair=[(x,y) for x in list4 for y in list5]
print(pair)
print(list4.append('husband_dad'))
print(list4)
print(list4.pop())
print(list4)
