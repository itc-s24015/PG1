list(range(1, 8))
print("{:04}".format(5))

str_num_list = map(lambda x: "{:04}".format(x), range(1, 8))
print(str_num_list)

print(list(str_num_list))
