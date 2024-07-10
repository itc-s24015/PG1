a = 100
if a >= 10:
    print(a)

a = 0
if a == 0:
     a += 1
     a *= 2
     a -= 1
print(a)

a = 709
if a % 15 == 0:
    print('fifteen')
elif a % 3 == 0:
    print('three')
elif a % 5 == 0:
    print('five')
else:
    pass

my_list =[0, 1, 4, 9, 16, 25, 36]
for i in my_list:
    if i % 2 == 0:
        print(i)


my_list = ['tokyo', 'osaka', 'fukuoka', 'aichi','kyoto','chiba','saitama','gunma']
my_list_6 = []
for s in my_list:
    if len(s) >= 6:
        my_list_6.append(s)
    print(my_list_6)


my_list = [1, 1, 2, 3, 5, 8, 13]
x = 0
for n in my_list:
    if n % 2 != 0:
        x += n
