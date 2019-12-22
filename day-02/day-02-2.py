puzzle_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 9, 19, 23, 1, 23, 5, 27, 2, 27, 10, 31, 1, 6, 31, 35, 1, 6, 35, 39, 2, 9, 39, 43, 1, 6, 43, 47, 1, 47, 5, 51, 1, 51, 13, 55, 1, 55, 13, 59, 1, 59, 5, 63, 2, 63, 6, 67, 1, 5, 67, 71, 1, 71, 13, 75, 1, 10, 75, 79, 2, 79, 6, 83, 2, 9, 83,
                87, 1, 5, 87, 91, 1, 91, 5, 95, 2, 9, 95, 99, 1, 6, 99, 103, 1, 9, 103, 107, 2, 9, 107, 111, 1, 111, 6, 115, 2, 9, 115, 119, 1, 119, 6, 123, 1, 123, 9, 127, 2, 127, 13, 131, 1, 131, 9, 135, 1, 10, 135, 139, 2, 139, 10, 143, 1, 143, 5, 147, 2, 147, 6, 151, 1, 151, 5, 155, 1, 2, 155, 159, 1, 6, 159, 0, 99, 2, 0, 14, 0]


def get_result(input_arr):
    for x1 in range(100):
        for x2 in range(100):
            arr = [x for x in input_arr]
            arr[1] = x1
            arr[2] = x2
            i = 0
            while True:
                op = arr[i]
                i1, i2, i3 = arr[i+1], arr[i+2], arr[i+3]
                if op == 1:
                    arr[i3] = arr[i1] + arr[i2]
                elif op == 2:
                    arr[i3] = arr[i1] * arr[i2]
                else:
                    assert op == 99
                    break
                i += 4
            if arr[0] == 19690720:
                print(x1, x2)
                #40, 19


get_result(puzzle_input)
