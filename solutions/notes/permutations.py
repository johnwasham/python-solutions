# permutations of an array, each perm is size of array, just in a different order (n! perms)

# O(n^2 * n!)

def permutations_iterative(nums):
    perms = [[]]

    for n in nums:
        next_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                next_perms.append(p_copy)
        perms = next_perms

    return perms


print(permutations_iterative([1, 2, 3, 4]))

