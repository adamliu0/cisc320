This program solves this knapsack problem of dogs eating the highest value of items in a list while maintaining their weight
to be less than or equal to their maximum weight capacity.

The program implements a dynamic programming algorithm to solve the knapsack problem. The algorithm works by constructing a table of subproblems, where each cell of the table represents the maximum value that can be achieved with a subset of the items and a limited capacity. The values in the table are calculated recursively, by comparing the value of including an item with the value of excluding it.

The worst-case runtime complexity of the program is O(nW), where n is the number of items and W is the numerical size of the capacity. This is because the program constructs a table of size (n+1) x (W+1), and fills in each cell of the table by comparing two values. The algorithm is therefore of runtime O(nW).