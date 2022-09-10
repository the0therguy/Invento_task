def get_aspected_index(two_pair_values, target_value):
    result = 0
    for i in range(len(two_pair_values)):
        if sum(two_pair_values[i]) == target_value:
            result = i

    return result


two_pair_values = [
    [1, 5],
    [9, -7],
    [0, 8],
    [6, 3],
    [4, 11],
    [14, 0],
    [8, 1],
    [4, 9],
]
target_value = 9
result = get_aspected_index(two_pair_values, target_value)
print(result)
