def two_sum(nums, target) -> list[int]:
    # 브루트 포스(Brute Force[정제않은, 난폭한 / 힘, 폭력]) 방식 : 원시적인 방법
    # -> 단점 : 느리다, 시간과 자원을 엄청나게 소비한다.
    # -> 장점 : 확실한다. 정확도가 100% 보장된다. 암호학에서 통용
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i ,j]

nums = [2, 7, 11, 15]
target = 9