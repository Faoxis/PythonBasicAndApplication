def searchChildren(classes, parent, child):

    if parent == child:
        return True

    if child in classes[parent]:
        return True

    for grandparent in classes[parent]:
        if searchChildren(classes, grandparent, child):
            return True
    return False


lst = []
classes = dict()

n = int(input())
for i in range(n):
    line = input().split(" ")
    if ':' in line:
        for i in range(2, len(line)):
            if classes.get(line[0]) is not None:
                classes[line[0]] += [line[i]]
            else:
                classes[line[0]] = [line[i]]
            if classes.get(line[i]) is None:
                classes[line[i]] = []
    else:
        for i in range(len(line)):
            classes[line[i]] = []

n = int(input())
for i in range(n):
    line = input().split()
    lst += [(searchChildren(classes, line[1], line[0]))]

# print(classes)
for i in range(len(lst)):
    if lst[i] == 0:
        print("Yes")
    else:
        print("No")

