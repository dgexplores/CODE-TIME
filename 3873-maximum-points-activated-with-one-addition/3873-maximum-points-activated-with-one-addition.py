class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]


class Solution:
    def maxActivated(self, points):
        x_id = {}
        y_id = {}
        idx = 0

        for x, y in points:
            if x not in x_id:
                x_id[x] = idx
                idx += 1
            if y not in y_id:
                y_id[y] = idx
                idx += 1

        dsu = DSU(idx)

        for x, y in points:
            dsu.union(x_id[x], y_id[y])

        comp_count = {}
        for x, y in points:
            root = dsu.find(x_id[x])
            comp_count[root] = comp_count.get(root, 0) + 1

        mx1 = mx2 = 0
        for c in comp_count.values():
            if c >= mx1:
                mx2 = mx1
                mx1 = c
            elif c > mx2:
                mx2 = c

        return mx1 + mx2 + 1