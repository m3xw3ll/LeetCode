def num_tile_possibilities(tiles):
    def dfs(path, t, s):
        if path not in s:
            s.add(path)
            for i in range(len(t)):
                dfs(path+t[i], t[:i] + t[i+1:], s)
        return len(s) - 1
    return dfs('', tiles, set())


print(num_tile_possibilities('AAB'))