def has_adjacent_same(val: str) -> bool:
    left = val[0]
    i = 1
    result = False
    while i < len(val):
        right = val[i]
        if left == right:
            result = True
            break
        left = val[i]
        i += 1
    return result


def no_larger_than(val: str) -> bool:
    left = val[0]
    i = 1
    result = False
    while i < len(val):
        right = val[i]
        if int(left) <= int(right):
            result = True
        else:
            result = False
            break
        left = val[i]
        i += 1
    return result


count = 0
for i in range(254032, 789860 + 1):
    if has_adjacent_same(str(i)) and no_larger_than(str(i)):
        count += 1

print(count)
# 1033
