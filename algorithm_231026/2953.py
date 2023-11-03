scores = []

for _ in range(5):
    score = [int(i) for i in input().split()] # [int, int, int, int]
    # score = []
    # for i in input().split():
    #     score.append(int(i))
    scores.append(sum(score))

max_score = max(scores)
max_index = scores.index(max_score) + 1
print(max_index, max_score)
    