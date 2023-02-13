This program solves the problem of summating a sequence of integers in a file while ignoring negative numbers and ending 
when it reads -999. The first number/line of the file should be a positive integer containing the length of the list of integers 
in the file (not including itself). The algorthm works by first checking if the first value is a positive integer. If not, then the 
program can safely return "EMPTY". In the case that the program does not return EMPTY, it proceeds to iterate through each value in 
the list of integers with a for loop. The program will break out of the for loop if it reads the value -999. Otherwise, it will 
only add the value of the current integer to the sum if it is a positive integer. Once it has iterated through all the integers, the 
program will return the sum.

This program has an algorithmic runtime of O(n) because it must iterate over each of the n integers in the file to see if it should 
add it to the sum, ignore it, or break out of the loop.
