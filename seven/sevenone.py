import re
import pathlib
from collections import defaultdict

ifp = open("input.txt", "r")

dirs = defaultdict(lambda: 0)
current_dir = pathlib.Path("/")
for line in ifp:
    command, arg = re.findall(r"(?:^\$ (cd|ls) ?(.*)$)?", line)[0]
    match command:
        case "cd":
            current_dir = current_dir / arg if arg != ".." else current_dir.parent
        case "cd" | "ls": continue

    size, name = re.findall(r"(?:^(\d+|dir) (.*)$)?", line)[0]
    if size.isdigit():
        dirs[current_dir] += int(size)
        for p in current_dir.parents:
            dirs[p] += int(size)

ifp.close()
print(sum((x for x in dirs.values() if x <= 100000)))
