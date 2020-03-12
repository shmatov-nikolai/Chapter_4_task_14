"""
14)Recursion: Davis Staircase(LRU cache)
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
"""

s = int(input().strip())
dict_stair = {1:1, 2:2, 3:4}

def recurs_stair(n):
    if n in dict_stair.keys():
        return dict_stair[n]
    else:
        dict_stair[n] = (recurs_stair(n-1)+ recurs_stair(n-2)+ recurs_stair(n-3))        
        return dict_stair[n]

list_Result = []
for j in range(s):
    n = int(input().strip())
    list_Result.append(recurs_stair(n))
     
print(list_Result)