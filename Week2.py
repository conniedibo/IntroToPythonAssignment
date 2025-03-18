#Create an empty list
my_list = []
print (my_list)

#Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print (my_list)

#Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print(my_list)

#Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

#Remove the last element from my_list
my_list.pop()
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30
index_30 = my_list.index(30)
print(index_30)

#Print the final list and the index of 30
print("Final List:", my_list)
print("Index of 30:", index_30)