# This will find out minimum path.
import heapq
import copy
import random


class Node:
    def __init__(self, level, path, bound=0):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound

    def __eq__(self, other):
        return self.bound == other.bound


def get_bound(node, w):
    path = []
    for i in node.path:  # because of index
        path.append(i - 1)
    bound = 0
    for i in range(0, len(path) - 1):
        bound = bound + w[path[i]][path[i + 1]]
    # if the edge is the last of node
    min_num = -1
    for i in range(0, len(w)):
        if i not in path:
            if min_num == -1:
                min_num = w[path[-1]][i]
            elif min_num > w[path[-1]][i]:
                min_num = w[path[-1]][i]
    bound = bound + min_num
    # if the edge is not last of node
    for i in range(0, len(w)):
        if i not in path:
            min_num = -1
            for j in range(0, len(w)):
                if j not in path[1:] and j != i:
                    if min_num == -1:
                        min_num = w[i][j]
                    elif min_num > w[i][j]:
                        min_num = w[i][j]
            bound = bound + min_num
    return bound


def get_length(node, w):
    length = 0
    path = []
    for i in node.path:
        path.append(i - 1)
    for i in range(0, len(path) - 1):
        length = length + w[path[i]][path[i+1]]
    return length


def TSP_BS(W):
    PQ = []  # initialize PQ to be empty
    v = Node(0, [1])
    v.bound = get_bound(v, W)
    min_length = -1  # min_length is infinity
    heapq.heappush(PQ, copy.deepcopy(v))
    u = Node(0, [])
    opt_tour = []
    tot_node = 0
    while PQ:  # PQ is not empty
        v = copy.deepcopy(heapq.heappop(PQ))
        tot_node = tot_node + 1
        if v.bound < min_length or min_length == -1:
            u.level = v.level + 1
            for i in range(2, len(W) + 1):
                if i not in v.path:
                    u.path = copy.deepcopy(v.path)
                    u.path.append(i)
                    if u.level == len(W) - 2:
                        for j in range(1, len(W) + 1):
                            if j not in u.path:
                                last = j
                        u.path.append(last)
                        u.path.append(1)
                        if get_length(u, W) < min_length or min_length == -1:
                            min_length = get_length(u, W)
                            opt_tour = copy.deepcopy(u.path)
                    else:
                        u.bound = get_bound(u, W)
                        if u.bound < min_length or min_length == -1:
                            if len(PQ) > 0:
                                c = heapq.heappop(PQ)
                                if c.level == u.level:
                                    if c.bound < u.bound:
                                        if random.randrange(0, c.level) > 0:
                                            if random.randrange(0, 2) == 0:
                                                heapq.heappush(PQ, copy.deepcopy(c))
                                            else:
                                                heapq.heappush(PQ, copy.deepcopy(c))
                                                heapq.heappush(PQ, copy.deepcopy(u))
                                        elif random.randrange(0, 10)  == 0:
                                            heapq.heappush(PQ, copy.deepcopy(u))
                                        else:
                                            heapq.heappush(PQ, copy.deepcopy(c))
                                            heapq.heappush(PQ, copy.deepcopy(u))
                                    else:
                                        if random.randrange(0, c.level) > 0:
                                            if random.randrange(0, 2) == 0:
                                                heapq.heappush(PQ, copy.deepcopy(u))
                                            else:
                                                heapq.heappush(PQ, copy.deepcopy(c))
                                                heapq.heappush(PQ, copy.deepcopy(u))
                                        elif random.randrange(0, 10) == 0:
                                            heapq.heappush(PQ, copy.deepcopy(c))
                                        else:
                                            heapq.heappush(PQ, copy.deepcopy(c))
                                            heapq.heappush(PQ, copy.deepcopy(u))
                                else:
                                    heapq.heappush(PQ, copy.deepcopy(u))
                            else:
                                heapq.heappush(PQ, copy.deepcopy(u))

    print("i am monte---------------------------------")
    print("the optimal path is : ", opt_tour)
    print("the min_length is : ", min_length)
    #return tot_node
    return min_length


# Set W as weight of edge.
W = [[0, 14, 4, 10, 20], [14, 0, 7, 8, 7], [4, 5, 0, 7, 16], [11, 7, 9, 0, 2], [18, 7, 17, 4, 0]]
TSP_BS(W)