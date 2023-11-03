def reorder_log_files(logs: list[str]) -> list[str]:
    letter_logs, digit_logs = [], []
    for i in logs:
        # isalpha() : 숫자면 False 문자면 True
        if i.split()[1].isalpha(): 
            letter_logs.append(i)
        else:
            digit_logs.append(i)
    # 정렬 함수에서 key는 정렬 기준을 정하는 함수명이 들어온다.
    # def my_sort(x):
    #     return x.split()[1:], x.split()[0]
    # letter_logs.sort(key=my_sort)
    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    print(letter_logs + digit_logs)


reorder_log_files(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])