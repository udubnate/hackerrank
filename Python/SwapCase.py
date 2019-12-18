def swap_case(s):
    out  = ""
    for c in s:
        if str(c).islower():
            out += c.capitalize()
        else:
            out += c.lower()
    return out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)