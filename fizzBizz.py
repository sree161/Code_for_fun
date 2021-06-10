arra = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in arra:
    div_3 = i % 3
    div_5 = i % 5

    if div_3 == 0 and div_5 == 0:
        print("fizzBizz")

    elif div_5 == 0:
        print("bizz")

    elif div_3 == 0:
        print("Fizz")

    else:
        print(i)