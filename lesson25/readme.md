This program solves the "Traveling Salesman Problem" of having a 2D adjacency matrix as input and finding the 
shortest path that visits every node and returns back to the first one. Additionally, the program also outputs 
the last number as the total distance traveled over this path.

The program makes a list of visited nodes and iterates through each node to get the minimum distance to travel to 
the next node. It checks this by checking if the node is not visited yet and if the distance to travel to it is 
less than the current minimum distance. If it meets these conditions, it becomes the new current minimum distance. 
At the end of the iteration, that node gets determined as the next node and the distance to travel to it gets added 
to the total distance traveled.

The run time of this algorithm is O(n^2) because we have to iterate through the matrix n times and each time we have 
to find the minimum value in the row which takes O(n) time so the total run time is O(n^2) + O(n) = O(n^2).