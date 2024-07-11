def fib2(n):
    '''nより小さなフィボナッチ数列絵をリストで返す'''
    result = []
    a, b = 0, 1
    while a < n:
        result append(a)
        a, b = b, a+b
        return result
