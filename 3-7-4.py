th open('number.txt','r') as f:
        sum = 0
        for data in f:
         num = int(data)
         sum += num
         print(sum)

