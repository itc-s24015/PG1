def make_circle_area_func(pi = 3.14):
    '''円の面積を計算する関数を作る'''

    def circle_area(radius):
        '''円の面積を計算する'''

        return radius * radius * pi

    return circle_area

# piが初期設定(3.14)のとき
circle_area_default = make_circle_area_func()
#piが3.1415926535のとき
circle_area_precise = make_circle_area_func(3.1415926535)

#2pi
print(circle_area_default(2))
print(circle_area_precise(2))
