# Key creation function
def create_key(cl, value):
    if value not in cl:
        cl[value] = list()


# Function for searching for values in the dictionary
def search(par, ch):
    try:
        if (par == ch) and (ch in classes):
            return 1
        elif par in classes[ch]:
            return 1
        else:
            for c in classes[ch]:
                if search(par, c):
                    return 1
            return 0
    except KeyError:
        return 0


classes = {}

for i in range(int(input())):
    values = input().split(" : ")
    if len(values) == 1:
        create_key(classes, values[0])
    else:
        child, parents = values[0], values[1].split(" ")
        for parent in parents:
            create_key(classes, child)
            classes[child].append(parent)

for q in range(int(input())):
    parent, child = input().split(" ")
    if search(parent, child):
        print("Yes")
    else:
        print("No")
