# This code is hard to read. Use Copilot to "Refactor" and "Explain" it.
def x(l):
    r = []
    for i in l:
        if i % 2 == 0:
            r.append(i * 3)
        else:
            r.append(i * 2)
    return sum(r)

def parse(s):
    # Messy string parsing
    parts = s.split(',')
    res = {}
    for p in parts:
        k, v = p.split(':')
        res[k.strip()] = int(v.strip())
    return res