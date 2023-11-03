def findContentChildren(self, g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    c_child = 0

    for child in g:
        for cookie in s:
            if g[child] <= s[cookie]:
                c_child += 1
                s.remove(cookie)
                break
    return c_child




