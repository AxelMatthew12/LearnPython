# x = 1;
# y = 2.8;
# z = 1j;

# print(type(x))
# print(type(y))
# print(type(z))

# thislist = ["apple", "banana", "chery", "apple","chery"]
# print(len(thislist))

"""   list item - Data stype
String , int and boolean data type :

list1 = ["apple", "banana", "cherry"]
list2 = [1,5,7,9,3]
list3 = [True,False , False]
"""
"Type ()"
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# list construktor
# thislist = list(("apple", "banana", "cherry"))
#note the double round-brackets
# print(thislist)

"If options"
# thislist = ["apple", "banana", "cherry" , "orange", "kiwi", "melon", "mango"]
# if "apple" in thislist:
#     print("Yes, 'apple' is in the fruits list ")

# Mengganti item value pada indeks tertentu

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "hitam"
# print(thislist)
"==========================================="



# thislist = ["apple", "banana", "cherry", "orange" , "kiwi", "mango"]
# # Change range of item values ==>
# # thislist[1:3] = ["watermelon"]
# # print(thislist)

# thislist.insert(2, "watermelon")
# print(thislist)

# thislist.append("orange")
# print(thislist)

# list1 = ["apple","banana", "cherry"]
# list2 = ["mango","pinapple", "papaya"]
# list1.pop()
# print(list1)

# del list2

"Loop concept"
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thatlist = ["apple", "banana", "cherry"]
[print(x) for x in thatlist]


