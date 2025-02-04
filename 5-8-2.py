multiplicated_xy_setdict = {frozenset([x, y]): x*y for x in range(2) for y in range(2)}
print(multiplicated_xy_setdict)

{0: {0: 0, 1: 0, 2: 0}, 1: {0: 0, 1: 1, 2: 2}, 2: {0: 0, 1: 2, 2: 4}}
multiplicated_xy_dict = {}
I = 3
J = 3
for i in range(I):
    multiplicated_xy_dict[i] = {}
    for j in range(J):
        multiplicated_xy_dict[i][j] = i*j
print(multiplicated_xy_dict)

multiplicated_xy_dict = {i:{j:(i*j) for j in range(J)} for i in range(I)}
print(multiplicated_xy_dict)

print(multiplicated_xy_dict[2][2])
