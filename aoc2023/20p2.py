import re


def make_ff():
    on = False

    def fn(_, pulse):
        nonlocal on
        if pulse == "H":
            return None
        else:
            on = not on
            return "H" if on else "L"

    return fn


def make_conj(senders):
    memory = {s: "L" for s in senders}

    def fn(sender, pulse):
        memory[sender] = pulse
        return "H" if "L" in memory.values() else "L"

    return fn


broadcaster = lambda _, pulse: pulse


plan = [re.findall("([%&a-z]+)", l) for l in open("./20.txt")]

cables = {h.strip("%&"): t for h, *t in plan}


def make_unit(name):
    global cables
    if name.startswith("%"):
        return make_ff()
    elif name.startswith("&"):
        name = name[1:]
        return make_conj([s for s in cables if name in cables[s]])
    else:
        return broadcaster


def press(
    cables,
    n=1000,
    initial=("button", "L", "broadcaster"),
    monitor=("L", "rx"),
    repeats=-1,
):
    global modules
    H, L = 0, 0
    last_detection = -1
    for i in range(n):
        todo = [initial]
        done = []
        while todo:
            sender, input_pulse, receiver = todo.pop(0)  # FIFO
            done.append((sender, input_pulse, receiver))
            if (input_pulse, receiver) == monitor:
                # print("Detected", monitor, "on press", i)
                if last_detection:
                    print("Cycle length", i - last_detection)
                last_detection = i
                repeats -= 1
            output_pulse = modules[receiver](sender, input_pulse)
            if output_pulse:
                todo.extend([(receiver, output_pulse, m) for m in cables[receiver]])
        H += sum(hl == "H" for _, hl, _ in done)
        L += sum(hl == "L" for _, hl, _ in done)
        if repeats == 0:
            break
    return H, L


# Thoughts on part 2
# - likely cycles of operation!
# - what are subgraphs that cycle...
# - we can then simplify the graph to just cyclic inputs and a final output
# - LCM probably
# - would need to make state centric to spot a cycle (return to past state)
# - currently state is buried
# - could keep a3 dict of name->state

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from(cables.keys())
G.add_edges_from([(n, out) for n, outs in cables.items() for out in outs])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
nx.draw_networkx_labels(G, pos)
plt.show()

"""
Notes on graphs:

broadcaster  -> 4 sub graphs: gd, kg, gt, lf
they have output nodes, gd->fv, kg->vt, gt->kk, lf->xr
output nodes just broadcast to next
final graph is:
vt, fv, kk, xr
these all go to sq, which is an &
need all these to message H
assuming these all message every time, then it's just the LCM of their cycles
"""


sub = [("gd", "fv"), ("kg", "vt"), ("gt", "kk"), ("lf", "xr")]

for input, output in sub:
    # reset network, just in case!
    modules = {h.strip("%&"): make_unit(h) for h, *_ in plan}
    sub_cables = {output: []}
    todo = [input]
    while todo:
        n = todo.pop()
        sub_cables[n] = cables[n]
        todo.extend(m for m in sub_cables[n] if m not in sub_cables)
    print("Subnetwork", input, output, sub_cables)
    _ = press(
        sub_cables,
        n=1000_000,
        initial=("broadcaster", "L", input),
        monitor=("L", output),
        repeats=2,
    )

from math import lcm

lcm(3863, 3797, 3931, 3769)

# Lessons/thoughts
# - instructions hard to follow, so started by manually constructing, which helped
# - code is pretty choppy, but approach of doing just enough to solve is healthy
# - more experienced coders will see a pattern and skip the earlier discovery
# - definitely learned LCM, todo.pop(), networkx from this competition
# - 100 lines of code including graph exploration isn't too bad

# david3x3x3 solution, with some edits from me, and comments

import math

graph = {
    (parts := line.rstrip().split(" -> "))[0]: parts[1].split(", ")
    for line in open("./20.txt")
} # warlus operator to get into one line; also no "modules", just named
res = []
for m in graph["broadcaster"]: # obvious way to identify subgraphs!
    nextl = [m] #aka todo
    num = 0
    len_num = 0
    while nextl:
        m2 = nextl[0]
        # decode chains of flip flops as bits in an integer
        g = graph["%" + m2]
        # flip-flops that link to a conjunction are ones
        # everything else is a zero
        num |= (len(g) == 2 or "%" + g[0] not in graph) << len_num
        len_num += 1
        nextl = [next_ for next_ in graph["%" + m2] if "%" + next_ in graph]
    res.append(num)
# find least common multiple of integers
print(math.lcm(*res))
