n = int(input())
time = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append((a, b))
time.sort(key=lambda x : (x[1], x[0]))      # 끝나는 시간 기준 정렬

end_time = 0
count = 0
for start, end in time :
    if start >= end_time :      # 겹치지 않으면 선택!
        count += 1 
        end_time = end          # 다음 회의는 이 end 이후여야 함
print(count)