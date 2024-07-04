print([2,4,8,16] + [3,6,9,12])
my_list = [2,4,8,16]
print(my_list + [3,6,9,12])
print(my_list)
my_list = [2,4,8,16]
my_list.append(3)
my_list.append(6)
my_list.append(9)
print(my_list)
my_list = [2,4,8,16]
my_list.extend([3,6,8,16])
print(my_list)
my_list = [2,4,8,16,3,6,9,12]
my_list.sort()
print(my_list)
my_list = [2,4,8,16,3,6,9,12]
my_list.sort(reverse=True)
print(my_list)
my_list = [2,4,8,16,3,6,9,12]
new_list = sorted(my_list)
rev_list = sorted(my_list, reverse=True)
print(my_list)
print(new_list)
print(rev_list)

