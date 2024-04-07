import re


def rule_fn(defn):
    if ":" not in defn:
        return lambda _: defn
    expr, to_name = re.match("(\w+[<>]\d+):(\w+)", defn).groups()
    return lambda xmas: to_name if eval(expr, xmas) else None


def parse_wf(wf):
    from_name, rules = re.match("([a-z]+){(.*)}", wf).groups()
    rule_fns = [rule_fn(defn) for defn in rules.split(",")]
    return from_name, rule_fns


section1, section2 = open("./19.txt").read().split("\n\n")
wfs = dict(parse_wf(wf) for wf in section1.split("\n"))
parts = [dict(re.findall("(\w)=(\d+)", p)) for p in section2.split("\n")]
parts = [{k: int(v) for k, v in part.items()} for part in parts]


def process_part(part):
    wf = wfs["in"]
    while True:
        for rule_fn in wf:
            next_wf_name = rule_fn(part)
            if next_wf_name:
                if next_wf_name in "AR":
                    return next_wf_name
                wf = wfs[next_wf_name]
                break  # new workflow


# part 1 - copy() otherwise some kind of corruption
print(sum(sum(p.values()) for p in parts if process_part(p.copy()) == "A"))

# 4HbQ code is jaw dropping! 

flows, parts = open("data.txt").read().split("\n\n")

A_ = lambda: 1 + x + m + a + s
R_ = lambda: 1
S_ = 0

exec(
    flows.replace(":", " and ")
    .replace(",", "_() or ")
    .replace("{", "_ = lambda: ")
    .replace("}", "_()")
)

exec(parts.replace(",", ";").replace("{", "").replace("}", ";S_+=in_()-1"))

print(S_)
