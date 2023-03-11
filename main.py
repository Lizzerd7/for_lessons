'''
import string
alphabet = string.ascii_lowercase
n = int(input())
M = []
for i in range(n):
    M.append(alphabet[i])
print(M)
'''

'''
n = int(input("Введите кол-во строк"))
M = []
for i in range(n):
    M.append(input())

x = input("Введите строки")
for s in M:
    if x in s:
        print(s)
'''

'''
s = input()
M = [int(i) for i in s.split()]
M.sort()
print(M)
M.reverse()
print(M)
print(sorted(M))
print(sorted(M, reverse=True))
'''


n = int(input())
M = []
# for i in range(1, n+1):
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        M.append(i)
        M.append(n // i)
print(M)

