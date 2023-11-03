import time

# 시간을 초단위(UTC: 협정세계표준시)로 반환
print(time.time())

# 연,월,일,시,분,초,요일,일년 중 몇 번째 날인지, 서머타임 여부
print(time.localtime())

# 문자열 반환 [요일 월 일 시:분:초 연도]
print(time.asctime())

# sleep(초) 만큼 딜레이
time.sleep(3)
print("3초가 지났습니다.")
