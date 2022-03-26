def solution(arr1, arr2):
    answer = [[sum([a*b for a, b in zip(ele1, list(ele2))]) for ele2 in zip(*arr2)] for ele1 in arr1]

    return answer

if __name__ == "__main__":
    arr1 = [[1, 4], [3, 2], [4, 1]]
    arr2 = [[3, 3], [5, 3]]
    print(solution(arr1, arr2))