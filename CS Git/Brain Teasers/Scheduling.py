import sys
# Input: `alice` and `bob` are the lists representing the respective schedules
#   for each student. Each availability schedule is represented as a list of tuples.
# Output: Return a single list of tuples representing the intervals
#   where both students are available.
def available(alice, bob):
    a = b = 0
    workingWindows = []
    while (a != len(alice) and b != len(bob)):
        currWindowAliceStart, currWindowAliceEnd = alice[a]
        currWindowBobStart, currWindowBobEnd = bob[b]
        # print (alice[a])
        # print(bob[b])
        # print()
        # print("------")
        if (currWindowAliceEnd < currWindowBobStart):
            a += 1
        elif (currWindowBobEnd < currWindowAliceStart):
            b += 1
        else:
            startMax = max(currWindowAliceStart, currWindowBobStart)
            endMin = min(currWindowAliceEnd, currWindowBobEnd)
            if (endMin - startMax > 0):
                workingWindows.append((startMax, endMin))
                
            if (currWindowAliceStart >= currWindowBobStart and currWindowAliceEnd <= currWindowBobEnd):
                a += 1
            elif (currWindowBobStart >= currWindowAliceStart and currWindowBobEnd <= currWindowAliceEnd):
                b += 1
            elif currWindowAliceStart > currWindowBobStart:
                b += 1
            elif currWindowBobStart > currWindowAliceStart:
                a += 1
            elif currWindowAliceEnd > currWindowBobEnd:
                b += 1
            else:
                a += 1
    return workingWindows
            
    
def main():
    a_lines = int(sys.stdin.readline())
    alice = []
    for _ in range(a_lines):
        line = sys.stdin.readline().strip().split(" ")
        alice.append((int(line[0]), int(line[1])))
    b_lines = int(sys.stdin.readline())
    bob = []
    for _ in range(b_lines):
        line = sys.stdin.readline().strip().split(" ")
        bob.append((int(line[0]), int(line[1])))
    print(available(alice, bob))
if __name__ == "__main__":
    main()
