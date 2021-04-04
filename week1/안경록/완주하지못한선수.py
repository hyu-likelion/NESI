def solution(p, c):
    p.sort()
    c.sort()
    lens = len(c)

    for i in range(0, lens):
        if (p[i] != c[i]):
            return p[i]
    return p[lens]