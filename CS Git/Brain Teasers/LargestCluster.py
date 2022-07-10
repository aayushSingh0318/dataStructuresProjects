#  File: LargestCluster.py
#  Description: Determine the largest cluster found in each journey through space.
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number:
import sys
# Input: s is a string representing your journey through the galaxy
# Output: return an integer representing the largest cluster encountered
def largest_cluster(s):
    largestSize = 0;
    currentCluster = None
    currentSize = 0
    for i in range(len(s)):
        if i == 0:
            currentSize = 1
            currentCluster = s[i]
        elif s[i] == currentCluster:
            currentSize += 1
        else:
            currentCluster = s[i]
            currentSize = 1
        
        largestSize = max(largestSize, currentSize)
    
    return largestSize

# IMPORTANT: You should not have to modify anything below this line
def main():
    # read in the number of test cases
    test_cases = int(sys.stdin.readline().strip())
    for i in range(test_cases):
        test_case = sys.stdin.readline().strip()
        max_cluster = largest_cluster(test_case)
        print("The largest cluster of journey", i, "is", max_cluster)
if __name__ == "__main__":
    main()