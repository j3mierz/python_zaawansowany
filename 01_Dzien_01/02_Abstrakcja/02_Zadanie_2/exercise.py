def middle_element(sequences):
    result = []
    for i in sequences:
        if len(i) % 2 == 0:
            result.append([i[int(len(i) // 2) - 1], i[int(len(i) / 2)]])
        else:
            result.append(i[int(len(i) / 2)])
    return result


print(middle_element([[1, 4, 2, 6, 7], [3, 4, '3', 'siema', 32, 5], [5, 6]]))
