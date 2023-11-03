# def reverse_string(s: list[str]) -> None:
#     s[:] = s[::-1]

# def reverse_string(s: list[str]) -> None:
#     s.reverse()

def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1

a = ["h","e","l","l","o"]
reverse_string(a)
print(a)