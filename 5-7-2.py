
prefecture_of_japan = {1: 'hokkaido', 2: 'aomori', 3: 'iwate'}
for x in prefecture_of_japan:
    print(x)

for x in prefecture_of_japan.keys():
    print(x)

for x in prefecture_of_japan.values():
    print(x)

for key, x in prefecture_of_japan.items():
    print(key, x)

list1 = [1, 2, 3]
list2 = ['hokkaidou', 'aomori', 'iwate']
print(dict(zip(list1, list2)))


