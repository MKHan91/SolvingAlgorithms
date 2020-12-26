input_ = input().split(' ')
N, X = int(input_[0]), int(input_[1])

subject = list(map(float, input().split(' ')) for _ in range(X))
for score in zip(*subject):
    print(sum(score) / len(score))