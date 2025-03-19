def dfs(n, lst):
    #종료 조건 n에 따라 값 리턴, 정답처리
    if n == M:      #M개를 고른 수열을 완성
        ans.append(lst)
        return
    
    for j in range(1, N+1): # N의 갯수만큼 검사
        if v[j]==0:
            v[j]=1
            dfs(n+1, lst+[j])
            v[j]=0
        

N, M = map(int, input().split())
ans = []
v = [0]*(N+1)

dfs(0, [])
for lst in ans :
    print(*lst)