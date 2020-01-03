# Enter your code here. Read input from STDIN. Print output to STDOUT

#number of test cases
T = input()

strarr = []

# create word arrays
for i in range(int(T)):
    strarr.append(input())

for str in strarr:
    # for each word seperate odds and evens
    odd = []
    even = []

    count = 0
    for c in str:
        if count % 2 == 0:
            even.append(c)
        else:
            odd.append(c)
        count += 1

    evenword = "".join(even)
    oddword = "".join(odd)
    print(evenword + " " + oddword)

