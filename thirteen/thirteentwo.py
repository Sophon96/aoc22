import functools


lines = [eval(line) for line in open("input.txt").readlines() if line.strip()] + [
    [[2]],
    [[6]],
]

cmpf = (
    lambda a, b, rec: next(
        (
            rt
            for rt in [
                (
                    isinstance(a[el], list)
                    and isinstance(b[el], list)
                    and rec(a[el], b[el], rec)
                )
                or (isinstance(a[el], list) and rec(a[el], [b[el]], rec))
                or (isinstance(b[el], list) and rec([a[el]], b[el], rec))
                or (-1 if a[el] > b[el] else (1 if a[el] < b[el] else 2))
                for el in range(min(len(a), len(b)))
            ]
            if rt != 2
        ),
        False,
    )
    or int(len(a) < len(b))
    or -(len(a) > len(b))
    or 2
)
wr1 = lambda a, b, f: -a if (a := f(a, b, f)) != 2 else 0
wr2 = lambda a, b: wr1(a, b, cmpf)

lines.sort(key=functools.cmp_to_key(wr2))
print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))
