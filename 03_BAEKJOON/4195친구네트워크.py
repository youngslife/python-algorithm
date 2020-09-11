import sys
sys.stdin.readline = open('input.txt', 'r')


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    X = find(x)
    Y = find(y)

    if X != Y:
        parent[Y] = X
        size[X] += size[Y]


for _ in range(int(input())):
    F = int(input())  # 친구 관계의 수 <= 100,000

    relation = {}  # name: idx
    parent = []  # parent[idx] = parent
    size = []  # size[idx] = size
    idx = -1

    for _ in range(F):
        f1, f2 = input().split()
        # print(parents)
        if not relation.get(f1):
            idx += 1
            relation[f1] = idx
            parent.append(idx)
            size.append(1)
        if not relation.get(f2):
            idx += 1
            relation[f2] = idx
            parent.append(idx)
            size.append(1)

        union(relation[f1], relation[f2])
        print(size[parent[relation[f1]]])