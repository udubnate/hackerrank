def mutate_string(string, position, character):
    arr = list(string)
    arr[position] = character

    return "".join(arr)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)