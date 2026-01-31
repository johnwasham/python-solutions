# update a value at index
# query a range L, R (for sum, etc)
# because we have the ability to update a value, we can't use prefix sum

# update - log n
# query - log n

# represented as array that we break into left/right halves going down the tree until you get to single index
# each node has left index, right index, and sum at that node
# get sum for a node by adding its left and right children
# all nodes have a left and right child


