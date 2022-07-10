from locale import ABDAY_1
import sys


# Return True if a and b are equivalent, False otherwise.
def equivalent(a: str, b: str) -> bool:
    lengtha = len(a)
    lengthb = len(b)
    a1= a[:lengtha//2]
    a2= a[lengtha//2:]
    b1= b[:lengthb//2]
    b2= b[lengthb//2:]
    
    
    if a == b:
        return True
    elif a1 == b1 and a2 == b2:
        return True
    elif a1 == b2 and a2 == b1:
        return True
    elif sorted(a1) == sorted(b1) and sorted(a2) == sorted(b2):
        return True
    elif sorted(a1) == sorted(b2) and sorted(a2) == sorted(b1):
        return True
    else:
        return False



def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    print(equivalent(a, b))


if __name__ == "__main__":
    main()
