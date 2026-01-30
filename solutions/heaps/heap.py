import heapq

pq = [82, 52, 2, 99, 8]

heapq.heapify_max(pq)
# heapq.heappush_max(pq, 3)

print(pq)

print(max(pq[1], pq[2]))

# while pq:
#     print(heapq.heappop_max(pq))

# print("len is " + str(len(pq)))
# print("---")

# pq = [82, 52, 99, 2, 8]
#
# heapq.heapify(pq)
#
# while pq:
#     print(heapq.heappop(pq))
#
# print("len is " + str(len(pq)))