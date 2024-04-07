from itertools import accumulate

cwd_list = []
dir_sizes = {}
for line in open("./7.txt"):
    line = line.strip()
    if line == "$ cd ..":
        _ = cwd_list.pop()
    elif line.startswith("$ cd "):
        dir = line[5:]
        if dir == "/":
            cwd_list = []
        else:
            cwd_list.append(dir)
    elif line == "$ ls" or line.startswith("dir "):
        pass
    else:
        assert not line.startswith("$")
        filesize, filename = line.split()
        filesize = int(filesize)
        for dir in ["/" + "/".join(d) for d in accumulate(cwd_list, initial="")]:
            dir_sizes[dir] = dir_sizes.get(dir, 0) + filesize
print(sum(s for s in dir_sizes.values() if s <= 100000))
total_space = 70_000_000
need_space = 30_000_000
unused_space = total_space - dir_sizes["/"]
min_dir_size = need_space - unused_space
print(min(s for s in dir_sizes.values() if s > min_dir_size))


