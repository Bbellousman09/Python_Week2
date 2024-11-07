# Create an empty list  
my_list = []  
print(my_list)

# Append elements to my_list  
my_list.append(10)  
my_list.append(20)  
my_list.append(30)  
my_list.append(40)  
print(my_list)

# Insert the value 15 at the second position (index 1)  
my_list.insert(1, 15)  
print(my_list)

# Extend my_list with another list  
my_list.extend([50, 60, 70])  
print(my_list)

# Remove the last element from my_list  
my_list.pop()  
print(my_list)

# Sort my_list in ascending order  
my_list.sort()  
print(my_list)

# Find and print the index of the value 30 in my_list  
index_30 = my_list.index(30)  
print(index_30)