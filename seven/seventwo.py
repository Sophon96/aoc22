import re
from pathlib import Path
from collections import defaultdict

ifp = open("input.txt", "r")

dirs = defaultdict(lambda: 0)
current_dir: Path = Path("/")
for line in ifp:
    arg1, arg2 = re.findall(r"(cd|ls|\d+|dir) ?(.*)$", line)[0]
    match arg1:
        case "cd":
            if arg2 == "..":
                current_dir = current_dir.parent
            elif arg2 == "/":
                current_dir = Path("/")
            else:
                current_dir /= arg2

        case "ls" | "dir": continue

        case _:
            dirs[current_dir] += int(arg2)
            for p in current_dir.parents:
                dirs[p] += int(arg2)

ifp.close()
needed_space = max(dirs.values()) - 40000000
print(min((x for x in dirs.values() if x >= needed_space)))
