
prefecture_of_japan = {1: "hokkaido", 2: "aomori", 3: "iwate"}
print(prefecture_of_japan)
print(prefecture_of_japan[1])
print(prefecture_of_japan.get(0))
print(prefecture_of_japan.get(1))
print(prefecture_of_japan.get(0, 'not Found'))
prefecture_of_japan[4] = 'miyagi'
print(prefecture_of_japan)
print(1 in prefecture_of_japan)
del prefecture_of_japan[4]
print(prefecture_of_japan)
print(prefecture_of_japan.pop(3))
print(prefecture_of_japan)
prefecture_of_japan.clear()
print(prefecture_of_japan)

