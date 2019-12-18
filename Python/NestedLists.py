# print("Enter input:")

nestedList = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nestedList.append([name,score])

# nestedList = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return (sorted(sub_li, key=lambda x: x[1]))

nestedList = Sort(nestedList)

found = False
firstLow = nestedList[0][1]
secondLow = 0
nameList = []

for name,score in nestedList:
    if not found:
        if score > firstLow:
            found = True
            secondLow = score

    if score == secondLow:
        nameList.append(name)

for name in sorted(nameList):
    print(name)
# print(nestedList)