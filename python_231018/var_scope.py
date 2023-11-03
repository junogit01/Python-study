# score = 100
# def score_change(score):
#     score -= 5
# score_change(score)
# print(score)

# 상단의 코드는 개발자의 의도에 맞지 않게, 100을 출력한다.
# 이를 개선하기 위해서는 global 키워드를 사용하거나, return문을 통해 score 값을 변경해줘야 한다.

# 1) global 사용하기
score = 100
def score_change():
    global score
    score -= 5

score_change()
print(score)

# 2) return문을 통해 score 값을 변경
score = 100
def score_change(score):
    score -= 5
    return score

score = score_change(score)
print(score)