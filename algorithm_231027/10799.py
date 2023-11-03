# 입력 ((())())
import sys
pipe = sys.stdin.readline().rstrip() # pipe = 파이프 입력을 받아온다. (뒤에 개행문자 제거)
pipe_count = 0
stack = []

for i in range(len(pipe)):
    # 여는 괄호 --> 쇠막대기 --> 스택에 저장
    if pipe[i] == "(": stack.append("(")
    # 닫는 괄호 --> 직전 괄호를 탐색
    else:
        # stack에서 하나가 제거되는 공통 부분
        stack.pop()
        # 직전괄호가 여는괄호 --> 레이저 --> 스택길이만큼 추가 [대신 stack에서 하나 제거]
        if pipe[i-1] == "(" : pipe_count += len(stack)
        # 직전괄호가 닫는괄호 --> 쇠막대기 끝 --> 1개 추가 [대신 stack에서 하나 제거]
        else : pipe_count += 1

print(pipe_count)