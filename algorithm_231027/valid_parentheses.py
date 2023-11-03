def isValid(s: str) -> bool:
    stack = []
    mapping = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    for i in s:
        # 열리는 괄호면 스택에 저장
        if i in mapping.values():
            print(f"{i}를 스택에 추가합니다.")
            stack.append(i)
        # 열리는 괄호가 아니고, 스택이 없거나 
        # 닫히는 괄호가 가장 맨 뒤 스택과 짝이 안맞는 경우
        elif not stack or mapping[i] != stack.pop():
            return False
    # 스택이 텅 비어있으면 T, 그렇지 않으면 F
    return not stack