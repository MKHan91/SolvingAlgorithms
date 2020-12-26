input_ = input().split(' ')
x1, k = input_[0], int(input_[1])
poly = input()

print(eval(poly.replace('x', x1)) == k)
