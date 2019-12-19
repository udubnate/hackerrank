def anyalnum(s):
    for c in s:
        if c.isalnum():
            return True
    return False

def anyalpha(s):
    for c in s:
        if c.isalpha():
            return True
    return False

def anydigit(s):
    for c in s:
        if c.isdigit():
            return True
    return False

def anylower(s):
    for c in s:
        if c.islower():
            return True
    return False

def anyupper(s):
    for c in s:
        if c.isupper():
            return True
    return False


if __name__ == '__main__':
    s = input()
print(anyalnum(s))
print(anyalpha(s))
print(anydigit(s))
print(anylower(s))
print(anyupper(s))



