"Nested Lists == 리스트 안에 있는 리스트"

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])

    score_list = [students[idx][1] for idx in range(len(students))]
    first_min = list(set(score_list))
    first_min.remove(min(first_min))
    second_min = min(first_min)

    for element in sorted(students):
        if second_min in element:
            print(element[0])

