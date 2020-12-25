def formingMagicSquare(s):
    # reform the array to one dimension
    s = s[0] + s[1] + s[2]
    # these are all forms of a 3x3 magic array
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
            [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    mini = 2**64
    # brute force the difference
    for arr in magic:
        diff = 0
        for i, j in zip(s, arr):
            diff += abs(i - j)
        mini = min(diff, mini)
    return mini