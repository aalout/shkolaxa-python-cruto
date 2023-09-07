n=int(input())

def guess(n):
        for i in range(1, n+1):
            if i*i== n:
                return i
            else:
                i = i + 1
            if i not in range(1, n+1):
                return "ne mogu tak"

a=guess(n)
print(a)