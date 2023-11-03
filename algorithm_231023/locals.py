a = 1
b = 2.0
c = "str"

# 로컬에 선언된 모든 변수를 조회할 수 있다.
# 디버깅에 유용하게 사용될 수 있다.
# 또한 로컬 스코프이기 때문에, 클래스나 함수 내부에서 조회가 가능하다!
print(locals())

import pprint

# 복잡한 구조를 예쁘게 보여준다.
pprint.pprint(locals())
