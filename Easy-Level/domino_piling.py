from math import floor
m,n = map(int,input().split())

#dominoes = m * n /2
dominoes = floor(m*n*0.5)

print(dominoes)

