#range of input
N = input()

#blank dictionary
phonebook = {}

def queryPhone(name):
    phone = phonebook.get(name,"Not found")
    if phone == "Not found":
        print("Not found")
    else:
        print(name + "=" + phone)

for i in range(int(N)):
    namephone = input()
    name, phone = namephone.split(" ")
    # add element to dictionary
    phonebook[name] = phone

#handling when there is no input left but queries larger than N
while True:
    try:
        queryPhone(input())
    except:
        break
