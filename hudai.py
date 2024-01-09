import math

def main():
    t = 0
    cin>> t
#C++ TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while(t--)
    while (t) != 0:
        t -= 1
        n = 0
        cin>> n
        a = [0 for _ in range(n)]
        j = 0
        for i in range(1, n + 1):
            a[j] = i
            j += 1

        Globals.print(a, n)
        print()
    t -= 1

class Globals:
    #C++ TO PYTHON CONVERTER WARNING: The following #include directive was ignored:
    ##include<bits/stdc++.h>
    @staticmethod
    def print(A, n):
        for i in range(0, n):
            if math.fmod(A[i], 2)==0:
                print(A[i], end = '')
                print(" ", end = '')
        for i in range(0, n):
            if math.fmod(A[i], 2)!=0:
                print(A[i], end = '')
                print(" ", end = '')

if __name__ == "__main__":
    main()
