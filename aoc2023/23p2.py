trail = {
    complex(i, j): c
    for j, line in enumerate(open("./23.txt"))
    for i, c in enumerate(line.strip())
    if c != "#"
}

H = int(max(x.imag for x in trail)) + 1
start = [pos for pos in trail if pos.imag == 0][0]
end = [pos for pos in trail if pos.imag == H - 1][0]

STEPS = 1, -1, 1j, -1j
neighbours = lambda u: tuple(u + s for s in STEPS if u + s in trail)

# Build graph by walking trail
nodes, edges = {start}, {}
todo = [(start, neighbours(start)[0])]
done = {start}
while todo:
    u, v = todo.pop()  # adjacent
    # Move forwards until hit node or end
    v_prev = u
    uv_len = 1
    while len(n := neighbours(v)) == 2:
        done |= {v}
        v_prev, v = v, n[0] if n[1] == v_prev else n[1]
        uv_len += 1
    # Add node and edges (in either direction)
    nodes |= {v}
    edges.setdefault(u, {})[v] = uv_len
    edges.setdefault(v, {})[u] = uv_len
    # If new node, add v->neighbours to todo
    if v not in done:
        done |= {v}
        todo.extend((v, x) for x in n)


def longest_path_to_end(u, skip_nodes=tuple()):  # returns None if no path to end
    if u == end:
        return 0
    max_path_len = 0
    for v in edges[u]:
        if v in skip_nodes:
            continue
        path_len = longest_path_to_end(v, skip_nodes + (v,))
        if path_len is not None:
            max_path_len = max(max_path_len, edges[u][v] + path_len)
    return max_path_len if max_path_len else None


print(longest_path_to_end(start, (start,)))

# Nice visualisation of solution (note, my data may differ)
# https://imgur.com/a/7YuZUTH

# Lessons:
# - This is an NP hard problem, worked this out myself, but could have checked wikipedia!
# - I got to the right method: simplify graph so you can brute force
# - I struggled with walking the graph. Others built the graph, then iteratively removed nodes with 2 edges.

# 4HbQ code is again, amazing!

G = {
    i + j * 1j: c
    for j, r in enumerate(open("./23.txt"))
    for i, c in enumerate(r.strip())
    if c != "#"
}  # same as mine

# generates all edges then collapses

E = {p: [p + d for d in (1, -1, 1j, -1j) if p + d in G] for p in G}


# this is similar to my walking along edge code, I think?
def collapse(p, n, d=1):
    while len(E[n]) == 2:
        p, n, d = n, [*{*E[n]} - {p}][0], d + 1
    return n, d


E = {p: [collapse(p, n) for n in E[p]] for p in G}


# Notes:
# - not passing seen around, so it's the same set being reused
# - again, similar to my search, seen is like my skip_nodes
# - resolves no route to end by just returning best so far
def search(node, dist, best, stop=[*G][-1], seen=set()):
    if node == stop:
        return dist
    if node in seen:
        return best

    seen.add(node)
    best = max(search(n, d + dist, best) for n, d in E[node])
    seen.remove(node)

    return best


print(search([*G][0], 0, 0))
