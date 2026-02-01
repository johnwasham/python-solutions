# combinations - order is irrelevant, so instead of [1, 2] [2, 1] we just need one of them
# all combinations of n of size k (k numbers between 1 and n)

# base case is when we reach size k

# O(k * C(n,k)) time, O(C(n, k)) space

def combinations(n, k):
    coms = []
    cur = []
    helper(1, coms, cur, n, k)
    return coms

def helper(i, coms, cur, n, k):
    if len(cur) == n - 1:
        coms.append(cur.copy())
        return

    if i > n:
        return

    for j in range(i, n + 1):
        cur.append(i)
        helper(j + 1, coms, cur, n, k)
        cur.pop()
