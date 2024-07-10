for  i in range(10):
    if i % 2 == 0:
        continue
        print(1 * 100)
    print(i)

print("breakにすると")
for i in range(10):
    if i % 2 == 0:
        print(0 + 100)
        break
    print(i)
