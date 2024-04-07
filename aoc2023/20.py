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
cables["rx"] = []


def make_unit(name):
    global cables
    if name.startswith("%"):
        return make_ff()
    elif name.startswith("&"):
        name = name[1:]
        return make_conj([s for s in cables if name in cables[s]])
    else:
        return broadcaster


modules = {h.strip("%&"): make_unit(h) for h, *_ in plan}
modules["rx"] = broadcaster
H, L = 0, 0
import time

t0 = time.time()
for i in range(1000_000):
    todo = [("button", "L", "broadcaster")]
    done = []
    while todo:
        sender, input_pulse, receiver = todo.pop(0)  # FIFO
        done.append((sender, input_pulse, receiver))
        # note, augmented instructions with: rx ->
        output_pulse = modules[receiver](sender, input_pulse)
        if output_pulse:
            todo.extend([(receiver, output_pulse, m) for m in cables[receiver]])
    # print(*done, sep="\n")
    H += sum(hl == "H" for _, hl, _ in done)
    L += sum(hl == "L" for _, hl, _ in done)

# part 1
print(H * L)
print(time.time() - t0)
