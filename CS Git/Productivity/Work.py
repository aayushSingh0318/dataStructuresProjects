#  File: Work.py 

#  Description:  Helper function num_lines allows for productivity to still be more than 1 line per coffee. 
#  Using this function, I conducted binary and linear seach and saaw the different times produced with the constant k.



import sys, time, math
def num_lines(v, k): #helper to count num of lines written
    coffee_count = 0 #number of cofees consumed
    lines_written = 0 
    while v // k ** coffee_count != 0: #ensures productivity is still more than 1 line per coffee
        lines_written += (v // k**coffee_count)
        coffee_count += 1 #coffee consumed
    return lines_written
         
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee

def linear_search(n: int, k: int) -> int:
    line_count = n + 1
    for num in range(line_count):
        if num_lines(num, k) >= n: #if the number of lines written exceeds the number required 
            return num
  # use linear search here


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee

#returns the midpoint
def binary_search (n: int, k: int) -> int:
    min = 0
    max = n
    while min <= max:
        midpoint = math.floor((min+max)/2) #full number 
        if num_lines(midpoint, k) >= n and num_lines(midpoint - 1, k) < n: 
            return midpoint
        elif num_lines(midpoint, k) >= n:
            max = midpoint - 1
        else:
            min = midpoint + 1
        
    


    
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
  main()
