import re

def solution(new_id):
    answer = ''

    # 소문자 치환
    new_id = new_id.lower()
    print(new_id)

    # 모든 문자 제거
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    print(new_id)

    # 2번 이상의 마침표 1번으로 치환
    new_id = re.sub("\.{2,}", ".", new_id)
    print(new_id)

    # 앞, 뒤 마침표 제거
    new_id = new_id.strip(".")
    print(new_id)

    # 빈 문자열이면 "a" 대입
    if not new_id:
        new_id = "a"
    
    # 만약 16자 이상이면 15개 문자를 제외한 나머지 문자 모두 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".": # 만약 제거 후 마침표(.)가 new_id의 끝에 있다면 끝에 위치한 마침표 제거
            new_id = new_id.rstrip(".")

    # 2자 이하이면 마지막 낱자를 반복해서 작성해서 최소 길이로 해당하게 만들기
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id
    return answer

id = "...!@BaT#*..y.abcdefghijklm"
solution(id)

