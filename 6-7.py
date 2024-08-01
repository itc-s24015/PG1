def reverse(data):
    '''引数に受け取ったシーケンスを逆向きに返す''' data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        #Myiteratorが__next__()を実装しているのでselfrをイテレータとして返す
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration()
        self.index = self.index - 1
        return self.data[self.index]
    
rev = R
    ret = []
    for index in range(len(data)-1, -1, -1):
        ret.append(data[index])
    return ret

for char in reverse('golf'):
    print(char, end=' ')