num_test_case = int(input())

for num in range(num_test_case):
    input_ = input().split(" ")
    a, b = input_[0], input_[1]
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as error:
        print("Error Code:", error)
    except ValueError as Verror:
        print("Error Code:", Verror)