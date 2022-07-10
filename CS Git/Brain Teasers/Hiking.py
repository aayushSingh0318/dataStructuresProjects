#  File: Hiking.py

#  Description: Help Me determine if he can finish the hike with the tools he has on hand. 


import sys

def hike(hike_string: str, capacity: int) -> bool:
    contents = {'p' : 'b' , 'm' : 'c' , 's' : 'f'}
    backpack_contents = []
    for pos in hike_string:
        if capacity > len(backpack_contents) and pos in list(contents.values()):
            backpack_contents.append(pos)
        elif pos in list(contents.keys()): 
            
            if len(backpack_contents) == 0:
                return False
            if contents[pos] != backpack_contents.pop():
                return False
    if len(backpack_contents) == 0:
        return True
    else: 
        return False
    
    
    
def main():
    first_line = sys.stdin.readline().split()
    N, W = int(first_line[0]), int(first_line[1])

    for _ in range(N):
        hike_string = sys.stdin.readline().strip()
        print(hike(hike_string, W))

if __name__ == "__main__":
    main()
