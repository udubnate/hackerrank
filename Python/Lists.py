if __name__ == '__main__':
    N = int(input())

arr = []


def remove(e):
    for item in arr:
        if int(item) == int(e):
            arr.remove(item)
            break

for _ in range(N):
    command = input()
    cmd = command.split(' ')

    #insert
    if cmd[0] == "insert":
        arr.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0] == "print":
        print(arr)
    elif cmd[0] == "remove":
        remove(cmd[1])
    elif cmd[0] == "append":
        arr.append(int(cmd[1]))
    elif cmd[0] == "sort":
        arr = sorted(arr)
    elif cmd[0] == "pop":
        arr.pop()
    elif cmd[0] == "reverse":
        arr.reverse()

#    print(cmd[0])
