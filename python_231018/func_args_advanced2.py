def hello_names(*names, count=1):
    """names를 count만큼 반복해서 출력
        (가변 매개변수, 키워드 매개변수) -> 테스트용
        결과 : 아! 가변 매개변수를 앞에 쓰면 되겠다!!!
    Args:
        names : 이름 목록
        count (int, optional): 반복 횟수. Defaults to 1.
    """
    for name in names:
        print(name * count)

hello_names("손흥민", "이강인", count=2)
# hello_names(2, "손흥민", "이강인") # 작동은 될 수 있으나, 원하는 동작이 아님!
# hello_names("손흥민", "이강인", 2) # 작동은 될 수 있으나, 원하는 동작이 아님!
# hello_names(count=2, "손흥민", "이강인") # 구문에러, 키워드 매개변수 뒤에 가변 매개변수 불가능!!!
# hello_names("손흥민", "이강인")