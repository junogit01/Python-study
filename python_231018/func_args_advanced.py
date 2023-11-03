def hello_names(count=1, *names):
    """names를 count만큼 반복해서 출력
        (키워드 매개변수, 가변 매개변수) -> 테스트용
        테스트 결과 : 키워드의 의미가 무색하다...
    Args:
        count (int, optional): 반복 횟수. Defaults to 1.
        names : 이름 목록
    """
    for name in names:
        print(name * count)

# help(hello_names)
hello_names(2, "손흥민", "이강인") # 가능
# hello_names("손흥민", "이강인", 2) # count = "손흥민" 불가능!!!
# hello_names(count=2, "손흥민", "이강인") # 구문에러, 키워드 매개변수 뒤에 가변 매개변수 불가능!!!
# hello_names("손흥민", "이강인") # count = "손흥민" 불가능!!!