class Sample:
    def __init__(self):
        self.a = 1
        self._b = 1
        self.__c = 1
        self.__d = 1
        self.__e = 1

    def show_attribute(self):
        a = self.a
        b = self._b
        c = self.__c
        d = self.__d_
        e = self.__e__
        print("a: {}, b: {}, c: {}, d: {}, e: {}".format(a, b, c, d, e))

s = Sample()
print(s.show_attribute())
