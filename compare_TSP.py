import random
import time
import TSP_DP
import TSP_BS
import TSP_BS_average


def random_matrix(n):  # it will generate a matrix n x n and diagonal is 0.
    matrix = [[0 for cor in range(n)] for row in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                matrix[i][j] = random.random()
    return matrix


print("Above is test case!---------------------------------------")

matrix_n = input("What is your wnat size of matrix? ")
performing = input("The number of execution? ")
dp_amount = 0
bs_amount = 0
bs_tot_node = 0
bs_avg_amount = 0
for i in range(int(performing)):
    matrix = random_matrix(int(matrix_n))

    start_time = time.time()
    TSP_DP.TSP_DP(matrix)
    end_time = time.time()
    dp_amount = dp_amount + end_time - start_time

    start_time = time.time()
    bs_tot_node = bs_tot_node + TSP_BS.TSP_BS(matrix)
    end_time = time.time()
    bs_amount = bs_amount + end_time - start_time

    start_time = time.time()
    TSP_BS_average.TSP_BS_avg(matrix)
    end_time = time.time()
    bs_avg_amount = bs_avg_amount + end_time - start_time

print("DP average : ", dp_amount / int(performing))
print("BS average : ", bs_amount / int(performing))
print("BS_avg average: ", bs_avg_amount / int(performing))
print("BS node average : ", bs_tot_node / int(performing))