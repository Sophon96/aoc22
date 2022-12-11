import re

with open("input.txt", "r") as ifp:
    inp = ifp.readlines()
    lines = [inp[n + 1 : n + 6] for n in range(0, len(inp), 7)]

monkeys = [
    {
        "inspected": 0,
        "items": list(map(int, re.findall(r"(\d+)", group[0]))),
        "op": re.findall(r"= (old (?:\+|\*) (?:old|\d+))", group[1])[0],
        "div_by": int(re.findall(r"(\d+)", group[2])[0]),
        "next": [
            int(re.findall(r"(\d+)", group[4])[0]),
            int(re.findall(r"(\d+)", group[3])[0]),
        ],
    }
    for group in lines
]


for _ in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            old = item
            new = eval(monkey["op"]) // 3
            monkeys[monkey["next"][(new % monkey["div_by"]) == 0]]["items"].append(new)
        monkey["inspected"] += len(monkey["items"])
        monkey["items"].clear()

top2 = sorted(monkeys, key=lambda x: x["inspected"], reverse=True)[:2]
print(top2[0]["inspected"] * top2[1]["inspected"])
