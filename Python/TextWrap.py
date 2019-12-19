import textwrap

def wrap(string, max_width):
    out = ""
    count = 0
    for c in string:

        if count % max_width == 0 and count != 0:
            out += "\n"
        count += 1
        out += c
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)