# May try to use this code
#Now, trying to find the index of a substring between specified indexes only
#print "Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9"
# print testString1.find('l',4,9)

def count_substring(string, sub_string):

    sublen = len(sub_string)

    count = 0
    for i in range(0, len(string)):
        if sub_string == string[i:(sublen+i)]:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)