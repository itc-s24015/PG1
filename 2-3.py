print(2e2)
print(32E2)
import sys
print(sys.float_info.max)
print(sys.float_info.min)
print(1.0 == 0.5 + 0.5)
print(0.3 == 0.1 + 0.1 + 0.1)
from decimal import Decimal
print(Decimal.from_float(0.5))
print(Decimal.from_float(0.3))
print(type(5))
print(type('a') is int)
print(type('a') is float)
print(isinstance('a', int))
print(pow(2,10))
print(pow(16,0.5))
print(pow(9,22,23))
print(2,3)
print(2.3)
print(2.672, 2)
print(2.3)
print(1, 2, 3, 4.5, 6.78)
print('abc')

name = input('お名前は')
print(name)

print(len(name))
name_iter = iter(name)
print(next(name_iter))
next(name_iter)
next(name_iter)
print(next(name_iter))
print(list(range(1,10))
print(list(2,11,2))
print(list(range(9,0,-2))
print(bin(7))
print(hex(15))
print("abc")
      print("aiu")
      print("i'm fine")
      print(type("xyz"))
zen_of_python = ''' The Zen of Python, by Tim Peters

Beautiful is brtter than ugly.
      Explicit is better than implicit.
      '''
      print(zen_of_python)

      my_str = 'この後改行\nしてからタブ\tで空白。'
      print(my_str)
      #これはコメントです
      pritn("a")#ここにも書ける
