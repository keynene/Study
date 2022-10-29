import sys
input = sys.stdin.readline

n = int(input().rstrip())
a,b = map(int, input().split())
m = int(input().rstrip())
people = [map(int, input().split())for _ in range(m)]

amap = [[] for _ in range(n+1)]
visited = [1e9]*(n+1)

for x,y in people:
    amap[x].append(y)
    amap[y].append(x)

def dfs(start, end, amap, dep):
    if start == end:
        visited[end] = min(visited[end],dep)
        return

    for i in amap[start]:
        if visited[i] > dep:
            visited[i] = dep
            dfs(i, end, amap, dep+1)

dfs(b, a, amap, 1)

if visited[a] == 1e9:
    print(-1)
else:
    print(visited[a])


##현진이 풀이

# import sys
# import copy

# def dfs (end , s , amap , count ) :

#     if s == end :
#         visited[end] = min (visited[end] , count )
#         return 
    
#     for i in amap[s] : 
#         if visited[i] > count : 
#             visited[i] = count 
#             dfs (end , i , amap , count+1 ) 

# n = int(input())

# a, b = map(int , input().split())

# case = int(input())
# amap = [[] for i in range(n+1)]
# visited = [999999]*(n+1)

# for i in range(case) : 
#     y , x = map(int , input().split())
#     amap[x].append(y)
#     amap[y].append(x)
 
# dfs(a , b  , amap , 1)
 
# if visited[a] == 999999 :  
#     print(-1)
# else : 
#     print(visited[a])    






# import sys
# ## 입력 받기



# n = int(sys.stdin.readline())

# a,b = map(int,sys.stdin.readline().split())

# m = int(sys.stdin.readline())

# amap = [[] for i in range(n+1)]
# visited = []

# for i in range(m) :
#     y , x = map (int , input().split())
#     amap[y].append(x)
#     amap[x].append(y)
    
    
# def dfs (amap , end , start , count , visited) :
  
  
#   if end == start :
#       print(count)
#       return  

#   for i in amap[start] :
#       if i not in visited :
#         temp = visited[:]  
#         temp.append(i)
#         dfs (amap , end , i , count + 1 , temp)

     
    
# dfs(amap , a , b   , 0 , visited)      





# from asyncio import constants
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# a,b = map(int, input().split())
# m = int(input().rstrip())
# people = [list(map(int,input().split())) for _ in range(m)]

# chon = [[0] for _ in range(n+1)]

# for i in range(1,n+1):
#     res = ''
#     for child in people:
#         parent = child[0]
#         if i == child[0]:
#             res += str(child[1])+' '
#     if len(res):
#         chon[i] = list(map(int, res.split()))

# cnt = 0
    
# def find_parent(chon, child):
#     global cnt
#     if child == a:
#         return cnt

#     for idx in range(1,len(chon)+1):
#         if child in chon[idx]:
#             parent = idx
#             cnt += 1
#             find_parent(chon, parent)

# print(find_parent(chon,a))


        

    




# def relation(idx,a,b):
#     global chon
#     if idx == n:
#         #9명 다 저장하면 실행할 코드
#         return 

#     people[idx]
