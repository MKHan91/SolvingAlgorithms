def solution(arr1, arr2):
    answer = [list(map(lambda x, y: x+y, arr1[idx], arr2[idx])) for idx in range(len(arr1))]
    return answer

def sumMatrix(arr1, arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]

if __name__ == "__main__":
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    print(solution(arr1, arr2))