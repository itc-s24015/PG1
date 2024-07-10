a, b = 0, 1
while b < 20:
    print(b)
    a, b = b, a + b

a = 0
while a < 100:
    if a > 10:
        break
    a += 2
    print(a)

print('ifの中にprint')
a = 0
while a < 100:
    if a > 10:
        print(a)
        break
    a += 2:
