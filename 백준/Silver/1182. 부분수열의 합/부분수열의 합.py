def sum_a (idx, current_sum, s_count):
    if idx == n :
        return 1 if current_sum == m and s_count > 0 else 0
    count1 = sum_a(idx+1, current_sum + a[idx], s_count+1)
    count2 = sum_a(idx+1, current_sum, s_count)
    
    return count1 + count2
n, m = map(int, input().split())
a = list(map(int, input().split()))

print(sum_a (0, 0, 0))