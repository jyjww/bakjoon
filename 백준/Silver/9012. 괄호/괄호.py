n = int(input())
for _ in range(n):
    a = input()
    stack = []
    for ch in a :
        if ch == '(' :
            stack.append(ch)
        elif ch == ')' :
            if stack and stack[-1] == '(':
                stack.pop()
            else :
                stack.append(ch)
    # print(stack)
    if not stack :
        print("YES")
    else:
        print("NO")
                    