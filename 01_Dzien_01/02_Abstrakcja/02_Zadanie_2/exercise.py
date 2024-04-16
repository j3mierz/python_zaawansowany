def middle_element(sequences):
    result = []
    for i in sequences:
        if len(i) % 2 == 0:
            result.append([i[int(len(i) // 2) - 1], i[int(len(i) / 2)]])
        else:
            result.append(i[int(len(i) / 2)])
    return result




class SequencesOfNumbers:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        result = range(self.start, self.stop, self.step)
        return len(result)

    def __getitem__(self, index):
        try:
            result = range(self.start, self.stop, self.step)[index]
        except IndexError:
            raise IndexError
        return result


a = SequencesOfNumbers(14, 46, 4)
print(len(a))
print(a[7])

print(middle_element([[1, 4, 2, 6, 7], [3, 4, '3', 'siema', 32, 5], [5, 6], a]))
