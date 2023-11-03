def solution(record):
    answer = []
    user_info = {}
    for x in record:
        command, uid, *_ = x.split()
        if command == 'Enter':
            user_info[uid] = x.split()[2]
        elif command == 'Leave':
            pass
        elif command == 'Change':
            user_info[uid] = x.split()[2]
    
    for x in record:
        command, uid, *_ = x.split()
        if command == "Enter":
            answer.append(f"{user_info[uid]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{user_info[uid]}님이 나갔습니다.")
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])