s = input()
left, right = [s[0]], [*s[-1:0:-1]]

m = int(input())
for i in range(m):
    cmd = input()

    if cmd == "prev" and len(left) > 1:
        right.append(left.pop())
    elif cmd == "next" and len(right) > 1:
        left.append(right.pop())
    elif cmd == "left" and len(left) > 1:
        left.pop()
    elif cmd == "right" and len(right) > 1:
        right.pop()

print(left[-1], right[-1])
