#Create an empty list of integers

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

another_list = [50,60,70]
my_list = my_list + another_list
print(my_list.pop(-1))

print(sorted(my_list))

if 30 in my_list:
    print(my_list.index(30))