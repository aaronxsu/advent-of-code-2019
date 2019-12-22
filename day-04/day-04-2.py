def has_adjacent_same(val: str) -> bool:
    left = val[0]
    i = 1
    matched_groups = []
    while i < len(val):
        right = val[i]
        is_left_right_same = left == right
        if len(matched_groups):
            last_matched = matched_groups[-1]
            if right in last_matched:
                matched_groups[-1] = (last_matched + right)
            elif is_left_right_same:
                matched_groups.append(left + right)
        else:
            if is_left_right_same:
                matched_groups.append(left + right)
        left = val[i]
        i = i + 1

    if len(matched_groups) == 0:
        return False
    else:
        return min([len(x) for x in matched_groups]) == 2


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
# 670
